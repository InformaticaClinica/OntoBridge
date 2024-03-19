# Introduction
This guide aims to streamline the process of transforming relational databases into Common Data Models using OntoBridge. It encompasses a detailed walkthrough of preparatory steps, essential configurations, and methodologies for the effective standardization and integration of clinical data.

# Preparing the Local Database for OntoBridge Integration
Preparing the local database is a crucial step before leveraging the OntoBridge framework for transforming the relational database content. Ensure that the local database is hosted on a DBMS that can be queried. This setup is necessary because OntoBridge is designed to interface smoothly with relational databases, allowing for efficient data retrieval and manipulation. Apart from the data stored in clinical events tables, local dictionaries and mapping tables should be created (if they did not exist). 

## Development of Dictionaries and Mapping Tables
Local dictionaries could already exist in the source database, but otherwise they would need to be created (usually holding a local code and its description, although they might be more complex according to the clinical subdomain). Typically, every concept of any column that could be reused throughout events tables should be included in these dictionaries (for example, diagnosis, codes for types of diagnosis, drug routes, medical units, etc). 

Standard dictionaries should be created according to the site’s needs and possibilities. In our case, we downloaded a database from OHDSI’s Athena with all the vocabularies we use. We then created a table that contains the subset of terms within Athena that are represented in our local dictionaries.

Mapping tables should contain the semantic mappings between local concepts (e.g., “SO2”) and standard concepts (e.g., SNOMED CT code 442440005). Ideally, mapping tables should at least represent the local code, the local domain, the standard vocabulary and the standard code. Since we focused on OMOP and i2b2 as CDMs thus far, our mapping table looks like this:

![Dictionary_example](/images/Dictionary_example.PNG)


In this example, local_uri refers to the name of the individual (after the namespace), local_ref is the local code, local domain refers to the domain within the local dictionaries, and the rest of the terms are either from OMOP (concept_code, concept_id, concept_name, vocabulary_id, omop_domain) or from i2b2 (concept_cd, concept_path). These tables are vital for ensuring consistency and interoperability with the target data model. 

# Ontologies
OntoBridge utilizes a structured approach to facilitate the integration and standardization of clinical data using ontologies. Here's a detailed explanation of the ontologies necessary for the OntoBridge pipeline:

## Local Data Model Ontology
This ontology has 2 two different parts with their own purpose: 

On the one hand, models the structure of the local database, including classes that represent tables or entities, properties that mimic the columns or attributes of these tables, and individuals that correspond to the different possible categorical results for properties. 

On the other hand, models the local codes used within the local database. These codes are represented as instances within the ontology, categorized and ordered by their relevant domains. This organization facilitates the identification and mapping of local codes to their standard counterparts, a critical step for data standardization and interoperability.

## Standard Model Ontologies

The standard model comprises two separate ontologies, each serving a distinct purpose in the standardization process:

Standard model ontology: This ontology contains the structure of the CDM. The ontology has the CDM tables modeled as rdf:Property metaclasses, with their table properties as sub-metaclasses from each CDM table. This structure helps in the process of mapping the local model with the CDM, which only has to be done once.

Standard Codes Ontology: This ontology contains the standard codes separated by their respective domains. It is essential for semantic mapping, allowing for the alignment of local codes with universally recognized standards, thereby ensuring that the data is both interoperable and semantically consistent.

![OMOP_Onto](/images/OMOP_example.PNG)

## Mapping Ontology
The mapping ontology includes mappings at two levels: 

Semantic Mappings: These are represented by sameAs triplets, which link local code instances to their standard equivalents, facilitating the semantic integration of data.

Syntactic Mappings: At this level, local properties (e.g., database columns) are mapped to properties in the CDM structure using the metaclasses (rdf:Property). This process enables the syntactic transformation of data from the local schema to the CDM schema, ensuring that the data not only fits into the standardized model but also retains its meaning and context.

## Clinical Events Ontology
The clinical events ontology imports the structure from the local database, which is contained within the local data model ontology. It is within this ontology that the data regarding patients' clinical events are subsequently inserted as instances. This process is detailed in the following sections.

# Transformation of Relational Database into RDF through Ontop

## Creation of the clinical data RDF files using Ontop
Ontop is a framework designed for data virtualization, providing a way to access relational databases through the abstraction layer of the Semantic Web. It allows users to map relational data to RDF (Resource Description Framework) graphs using SQL queries as a bridge. 

## Ontop Materialize 
Ontop Materialize is a specific functionality within the Ontop framework that allows for the generation (or "materialization") of RDF triples from relational databases based on predefined mappings. 

Steps to Use Ontop's Materialize Tool

1. Define R2RML Mappings: Before using the materialize tool, R2RML mappings must be defined. These mappings specify how tables and columns in the relational database correspond to RDF individuals, classes and properties.

2. Configuration: Ontop must be correctly configured with the database connection details, this is done in the properties file

3. Running the Materialize Tool: This process will read the database using the R2RML mappings and generate RDF triples.

4. Output: The output will be a set of RDF triples in the chosen format (e.g., Turtle, RDF/XML, etc.).

# Insertion of the Clinical Events data into the Clinical Event Ontology

## R2RML Standard codes

To apply OntoBridge effectively, it is crucial to have an ontology with the standard codes to be used in the CDM. For this purpose, it is necessary to construct an R2RML that transforms all the standard codes stored within the standard codes dictionary. To achieve this, a ttl file containing these mappings must be created. The following is an example of mapping for the OMOP CDM, where each part of the mapping document is explained.

Prefix Declarations: The mapping file begins with declarations of prefixes to simplify notation. Notably, the prefix rr denotes the R2RML namespace http://www.w3.org/ns/r2rml#, and stc points to a specific ontology at http://ontoar.clinic.cat/ontologias/standard_concepts.owl#. These prefixes enhance the readability and ease of writing in the Turtle format.

Logical Table and SQL Query: The rr:logicalTable component within a mapping specifies the source of the data, which, in this instance, is defined by a SQL query.

Subject Maps and Predicate-Object Maps: The mappings include rr:subjectMap for defining RDF subjects and rr:predicateObjectMap for detailing the predicates and objects, thus forming RDF triples. These mappings establish connections between database fields and specific OMOP ontology concepts.

## R2RML Clinical events
Clinical events data must be transformed into RDF format so that it can later be inserted into the ontology. For this purpose, a ttl file must also be constructed to map the local clinical data placed in the local dictionary to RDF. The following example shows how patient data, specifically the date of birth and date of death, are transformed into RDF format.

![mapping_example](/images/mappng_example.PNG)

## R2RML Local concept codes
In a similar way to that described for inserting standard codes into the ontology, local codes must also be inserted within the onology that models the local data model. To do this, a ttl file must be built that transforms the data stored in the local dictionary into RDF.

## R2RML SameAs
Finally, the mapping between local variables and standard ones can also be performed using a TTL with Ontop, where the relationship of sameAs is established between the different instances to be mapped. For this purpose, the dictionary is used that maps local concepts to standards.

## Isertion of clinical events data to OWLs
Once the RDFs are created, they are inserted into the respective ontologies with the Python script rdf_to_owl.py

Specifically, 4 insertions are made:

The RDF of the local code dictionaries is inserted into the local data model ontology.

Standard codes are inserted into the ontology of the standard model

Data from clinical events are inserted into the clinical events ontology.

Mappings between standard and non-standard codes are inserted into the mapping ontology

## Extraction of the standard data tables
To extract the standard data, the following steps must be followed:

1. Uploading the Set of Ontologies to Jena Fuseki: The first step involves uploading a set of ontologies into Jena Fuseki (a popular open-source SPARQL server). 

2. Executing SPARQL Queries Using the SPARQLWrapper Python Library: Once the ontologies are uploaded, query this data to extract the CDM tables using SPARQL. The code to perform these queries using python is located in the "Table_creation" folder

3. Post-Processing in Python to Adjust Tables to the specific CDM (for example, OMOP) and extract data as CSV: After retrieving the necessary information from the ontologies, the post-processing is performed. This involves transforming the query results into a format that aligns with that of the CDM. Finally, CDM data tables are extracted in CSV format and ready to be loaded into a DBMS or directly used for analysis.


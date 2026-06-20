# OntoBridge

**OntoBridge** is an open-source tool for transforming local clinical databases into multiple Common Data Models through a **single semantic transformation pipeline**.

Developed by the **Clinical Informatics Team at Hospital Clínic de Barcelona**, OntoBridge simplifies the conversion of relational clinical data into standards such as **OMOP** or **i2b2** by leveraging ontologies and semantic mappings.

---

## Overview

OntoBridge enables both **semantic** and **syntactic interoperability** by representing:

* Local database schemas
* Clinical events and concepts
* Standard clinical data models and vocabularies
* Mappings between local and standard concepts

The framework converts relational data into RDF and extracts standardized datasets through SPARQL queries and Python-based post-processing.

---

## Features

* Transform local relational databases into standardized clinical data models.
* Represent local and standard data structures using ontologies.
* Convert SQL data into RDF using **Ontop Materialize**.
* Extract standardized tables through **SPARQL** and **Python** workflows.
* Support multiple target standards through a single transformation pipeline.
* Provide a fully **Dockerized workflow** for simplified deployment and execution.

---

# Architecture

```text
Relational Database
        │
        ▼
Local Ontologies + Semantic Mappings
        │
        ▼
Ontop Materialize
(SQL → RDF)
        │
        ▼
RDF + OWL Ontology System
        │
        ▼
Apache Jena Fuseki
        │
        ▼
SPARQL Extraction
        │
        ▼
Python Post-processing
        │
        ▼
Standardized CSV Files
```

---

# Main Workflow

## 1. Prepare the Local Database

Before starting:

* Ensure the database is accessible and queryable.
* Create local dictionaries and mapping tables when necessary.
* Identify and document local clinical concepts.

---

## 2. Build the Ontologies

OntoBridge relies on several interconnected ontologies:

* **Local Model Ontology**
* **Clinical Events Ontology**
* **Standard Model Ontology**
* **Standard Codes Ontology**
* **Mapping Ontology**

These ontologies provide the semantic layer required to transform local data into standard representations.

---

## 3. Generate RDF from Relational Data

Using **Ontop Materialize**:

1. Define mappings from SQL tables and columns to RDF classes and properties.
2. Materialize RDF triples from the relational database.

---

## 4. Extract Target CDM Tables

1. Upload the ontologies to **Apache Jena Fuseki**.
2. Execute SPARQL-based extraction queries.
3. Apply Python post-processing.
4. Export the final standardized tables as CSV files.

---

# Supported Target Models

* **OMOP CDM**

  * Version 5.3
  * Version 5.4
  * Version 6.0
* **i2b2**

---

# Requirements

* Queryable relational DBMS
* Local ontology representing the source database
* Docker
* Docker Compose

**Recommended DBMS:** MySQL

---

# Quick Start

Start the services:

```bash
docker-compose up -d
```

Then:

1. Open the OntoBridge interface in your browser.
2. Enter your SQL database connection parameters.
3. Generate RDF from your local data.
4. Select the target standard.
5. Create the standardized model tables.

The resulting CSV files will be generated inside the:

```text
data/
```

directory.

---

# Purpose

OntoBridge promotes:

* Open Science
* Data Democratization
* Semantic Interoperability
* Reusability of Clinical Data
* Multi-standard Healthcare Data Integration

Its goal is to make local healthcare data reusable across multiple standards and facilitate interoperability in clinical research and real-world evidence generation.

---

## Citation

If you use OntoBridge in your research or projects, please cite the corresponding publication from the Clinical Informatics Team at Hospital Clínic de Barcelona.

# Ontobridge: A Tool for Normalizing Medical Data Based on Ontologies

## Introduction to OntoBridge
Ontobridge, created by the Informàtica Clínica group at Hospital Clínic de Barcelona, is an innovative tool designed to enhance the sharing and analysis of medical data by transforming local databases into standardized data models. Leveraging the principles of ontologies, it offers a structured and semantic approach to data management, which improves data interoperability, consistency, and the integration of various data sources. Initially compatible with OMOP and i2b2, Ontobridge aims to expand its support to other CDMs like MIMIC and ICGC Argo, underlining its potential to boost medical research and global data exchange. This tool underscores a commitment to open science through the use of freely accessible software.

## Softwares

### Ontop
Ontop is a framework that allows users to transform relational databases into RDF graphs, which can then be queried with SPARQL. It is essential for OntoBridge as it is the gateway for ontological representation of source databases.

**Installation:** Visit the Ontop website [Ontop website](https://ontop.inf.unibz.it/) and follow the instructions to download and install Ontop for your operating system.

### Python
Installation: Download Python from the official website [Python website](https://www.python.org/downloads/). Ensure you install Python 3.6 or newer.

**Required Python Libraries:** OntoBridge relies on several Python libraries for data handling, web requests, file operations, RDF manipulation, and more. You can install these libraries using pip, Python's package installer.
```bash
pip install glob2 requests os-win subprocess32 rdflib datetime time python-csv SPARQLWrapper pandas
```

### Protégé
Protege is an open-source ontology editor and a framework for building intelligent systems. Its visual interface facilitates the management and visualization of ontologies.

**Installation:** Download and install Protege from its official website [Protégé website](https://protege.stanford.edu/).

# Documentation

[Documentation](Documentation/documentation.md)

# License

[License](License/License.txt)

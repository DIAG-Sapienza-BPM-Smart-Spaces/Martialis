# Martialis - An Open Framework for Knowledge Graphs-based Retrieval Augmented Generation
## Overview
Martialis is a next-generation framework designed to enhance the performance of **Large Language Models (LLMs)** in solving complex linguistic tasks in domain-specific contexts (e.g., healthcare, legal, manufacturing). By integrating **Knowledge Graphs** (KGs) and **Ontologies**, Martialis provides accurate answers and generates structured, domain-specific texts.

## Key Innovations
* _Domain-Specific Knowledge Integration_: combines sub-symbolic (LLMs) and symbolic AI (Knowledge Graphs) for enhanced reasoning.
* _Advanced Retrieval-Augmented Generation (RAG)_: augments traditional RAG techniques with domain-specific KGs for precise responses.
* _Ontology-Based Validation_: ensures generated outputs align with predefined ontologies, improving consistency and reliability.
* _Open-Source and Modular_: fully customizable for diverse domains and use cases.

## ARCHITECTURE
The framework is built with a modular architecture, enabling customization and adaptability to various use cases. Each module can be replaced or extended to meet specific requirements.

The core components of Martialis are:

1. **Automatic KG-Extractor**: automatically generates domain-specific KGs from unstructured documents, providing a structured representation of the domain's knowledge.

2. **Advanced Retrieval-Augmented-Generation (RAG)**: enhances the standard RAG pipeline by integrating domain-specific KGs to support reasoning and generate accurate responses to complex queries.

3. **Ontology-Based Validator**: ensures the generated outputs align with predefined ontologies, validating their structure and content to guarantee consistency and compliance.

Complete Martialis' architecture is presented below:

![MARTIALIS' ARCHITECTURE](https://github.com/user-attachments/assets/4fd06701-728f-44aa-b5b0-61d0dbf2ef87)

Martialis is designed to address two primary types of domain-specific linguistic tasks:

### Question Answering (QA)
Martialis can answer complex questions by leveraging its *Advanced Retrieval-Augmented-Generation (RAG) Module*.

When a user poses a question, the framework retrieves relevant context from the domain-specific documents stored in its **Vector Database**.
It then integrates this context with the structured information in the Domain Knowledge Graph to enhance reasoning and generate precise answers.

### TEXT GENERATION
Martialis has great capability in generating structured, domain-specific texts using its *Ontology-Based Validator Module*.

Users can request detailed outputs. The framework first retrieves relevant entities and properties from the domain ontology to construct a blueprint for the requested text. It then validates the generated text by comparing its structure and content against the ontology, assigning a confidence score to indicate compliance.

# GETTING STARTED
This guide will help you set up Martialis and run your first tasks for question answering and text generation.

## INSTALLATION
First of all, clone the repository:


```bash
git clone https://github.com/DIAG-Sapienza-BPM-Smart-Spaces/Martialis.git
```

```bash
cd Martialis
```

Before starting, ensure you have the required libraries listed in the requirements.txt file:

```bash
pip install requirements.txt
```






## CONFIGURATION

## RUNNING

## EXAMPLE USE CASE

## DOCUMENTATION

# Martialis - An Open Framework for Knowledge Graphs-based Retrieval Augmented Generation

## Overview
Martialis is a next-generation framework designed to enhance the performance of **Large Language Models (LLMs)** in solving complex linguistic tasks in domain-specific contexts (e.g., healthcare, legal, manufacturing). By integrating **Knowledge Graphs** (KGs) and **Ontologies**, Martialis provides accurate answers and generates structured, domain-specific texts.

### Key Innovations
* _Domain-Specific Knowledge Integration_: combines sub-symbolic (LLMs) and symbolic AI (Knowledge Graphs) for enhanced reasoning.
* _Advanced Retrieval-Augmented Generation (RAG)_: augments traditional RAG techniques with domain-specific KGs for precise responses.
* _Ontology-Based Validation_: ensures generated outputs align with predefined ontologies, improving consistency and reliability.
* _Open-Source and Modular_: fully customizable for diverse domains and use cases.

## TABLE OF CONTENT 
1. [Architecture](#architecture)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running](#running)
5. [Example use case](#example-use-case)
6. [Documentation](#documentation)

## Architecture
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

### Text Generation
Martialis has great capability in generating structured, domain-specific texts using its *Ontology-Based Validator Module*.

Users can request detailed outputs. The framework first retrieves relevant entities and properties from the domain ontology to construct a blueprint for the requested text. It then validates the generated text by comparing its structure and content against the ontology, assigning a confidence score to indicate compliance.

# Getting Started
This guide will help you set up Martialis and run your first tasks for question answering and text generation.

## Installation
First of all, clone the repository:


```bash
git clone https://github.com/DIAG-Sapienza-BPM-Smart-Spaces/Martialis.git
```

```bash
cd Martialis
```

Before starting, ensure you have the required libraries listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

## Configuration
After cloning the repository, you need to configure the `.env` file with the correct values for your environment. Follow these steps: 

1. copy the file `.env.sample` as file `.env` using the following command
```bash
cp .env.sample .env
```

2. Update variables in the `.env` file:
 * `OPEN_API_KEY`: your openai api key
 * `LLAMA_API_KEY`: your llama api key (check: https://cloud.llamaindex.ai/login)
 * `MISTRAL_API_KEY`: your mistral api key
 * `NEO4J_USERNAME`: username from neo4j DB
 * `NEO4J_PASSWORD`: password from neo4j DB
 * `NEO4J_URL`: bolt://localhost:7687

## Running
Coming soon

## Example use case
Coming soon

# Documentation
For more detailed information on the underlying concepts and methodologies that Martialis is based on, please refer to the following papers:

1. **Bianchini F., Calamo M., De Luzi F., Macrì M and Mecella M. (2024)** - [*Enhancing Complex Linguistic Tasks Resolution through Fine-tuning LLMs, RAG, and Knowledge Graphs*](https://doi.org/10.1007/978-3-031-61003-5_13)
   This paper introduces the integration of Knowledge Graphs into the RAG framework to solve complex linguistic tasks in domain-specific contexts. It lays the foundation for the approach used in Martialis, focusing on improving LLM capabilities by incorporating structured knowledge.

2. **Bianchini F., Calamo M., De Luzi F., Macrì M and Mecella M. (2024)** - [*A Service-Based Pipeline for Complex Linguistic Tasks Adopting LLMs and Knowledge Graphs*](https://doi.org/10.1007/978-3-031-72578-4_8)  
   This work presents a service-based framework that adapts LLMs and Knowledge Graphs to provide precise answers and domain-specific text generation. It discusses the modular architecture and the potential for applying Martialis across various industries, including healthcare and law.


---

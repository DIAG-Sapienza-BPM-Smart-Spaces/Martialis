'''
PER ORA FACCIAMO CHE FUNZIONA SELEZIONANDO UN SINGOLO FILE, STO ESPLORANDO L'INTEGRAZIONE DI VECTOR DB COME:
  -pinecone
  -weaviate
  -milvus
'''

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Patch  
import io  
import numpy as np 
import csv  
import pandas as pd  

# Additional libraries for advanced functionality (commented out unless needed):
# from torchvision import transforms  # For image transformations (uncomment if used)
# from transformers import AutoModelForObjectDetection  # For AI models (uncomment if needed)

import torch  
import openai  
import os  
import fitz  

# To prevent asyncio-related issues in environments like Jupyter Notebook:
import nest_asyncio
nest_asyncio.apply()

# GUI handling for file selection dialogs:
import tkinter as tk
from tkinter import filedialog

# For progress tracking in loops:
from tqdm.autonotebook import tqdm

#For private info upload
from dotenv import load_dotenv

# For Llama index functionalities
from llama_parse import LlamaParse  
from llama_index.core.node_parser import MarkdownElementNodeParser 
from llama_index.llms.openai import OpenAI    
from llama_index.core import VectorStoreIndex
from llama_index.core import PropertyGraphIndex

# =====================
#   KEY LOADING
# =====================

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llama_api_key = os.getenv("LLAMA_API_KEY")

if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    print("OpenAI API key loaded successfully.")
else:
    print("OpenAI API key not found in .env file.")

if llama_api_key:
    os.environ["LLAMA_API_KEY"] = llama_api_key
    print("Llama API key loaded successfully.")
else:
    print("Llama API key not found in .env file.")
  
# =====================
#   FILE SELECTION
# =====================

def select_file():
    root = tk.Tk()  
    root.withdraw()  
    
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("File OWL, PDF e TXT", "*.owl *.pdf *.txt"), ("All files", "*.*"))
    )
    return file_path

selected_file = select_file()
if selected_file:
    print(f"You selected: {selected_file}")
else:
    print("None file selected")

# ================================
#   DOCUMENT PARSING AND INDEXING
# ================================

parser = LlamaParse(
    os.environ["LLAMA_API_KEY"] = llama_api_key,
    result_type="markdown" # other options json, text, html, raw                                      
)
documents = await parser.aload_data(selected_file)
Print(f'Document {selected_file} correctly parsed')

''' DA TOGLIERE
node_parser = MarkdownElementNodeParser(
  llm=OpenAI(model="gpt-4-turbo"),
  num_workers=4) 
'''
#DEFINIRE MEGLIO
#nodes = node_parser.get_nodes_from_documents(documents)
#base_nodes, objects = node_parser.get_nodes_and_objects(nodes)
#recursive_index = VectorStoreIndex(nodes=base_nodes+objects)

index = VectorStoreIndex.from_documents(documents)
Print(f'Document {selected_file} correctly indexed')

# =====================
#   DOCUMENT INDEXING
# =====================

query_engine = index.as_query_engine(similarity_top_k = 2)
response = query_engine.query(user_query)
retrieved_nodes = response.source_nodes
retrieved_list = [node.text for node in retrieved_nodes]




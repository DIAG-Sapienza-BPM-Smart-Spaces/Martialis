'''
PER ORA FACCIAMO CHE FUNZIONA SELEZIONANDO UN SINGOLO FILE, STO ESPLORANDO L'INTEGRAZIONE DI VECTOR DB COME:
  -pinecone
  -weaviate
  -milvus
'''
import torch  
import openai  
import os  
import fitz  

#For RDF handling
from rdflib import Graph


# To prevent asyncio-related issues in environments like Jupyter Notebook:
import nest_asyncio
nest_asyncio.apply()

# GUI handling for file selection dialogs:
import tkinter as tk
from tkinter import filedialog
import pprint

# For progress tracking in loops:
from tqdm.autonotebook import tqdm

#For private info upload
from dotenv import load_dotenv

# For Llama index functionalities
from llama_parse import LlamaParse  
from llama_index.core import Document, VectorStoreIndex, PropertyGraphIndex
from llama_index.core.node_parser import MarkdownElementNodeParser 
from llama_index.llms.openai import OpenAI  

# Additional libraries for advanced functionality (commented out unless needed):
# from torchvision import transforms  # For image transformations (uncomment if used)
# from transformers import AutoModelForObjectDetection  # For AI models (uncomment if needed)

# =====================
#   KEY LOADING
# =====================

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llama_api_key = os.getenv("LLAMA_API_KEY")
mistral_api_key = os.getenv("MISTRAL_API_KEY")

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

if mistral_api_key:
    os.environ["MISTRAL_API_KEY"] = mistral_api_key
    print("Mistral API key loaded successfully.")
else:
    print("Mistral API key not found in .env file.")
  
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
#   MODEL SELECTION
# ================================
model_list = {'OpenAI': ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo', 'gpt-3.5-turbo'],
              'Mistral': ['mistral-large-latest', ],
              'Llama': []}

def select_model():
  family_model= input(
    '''Please select which family model do you prefere:
        1. OpenAI 
        2. Mistral
        3. Llama
        '''
  if family_model == '1':
    model=input('''Please select which model (not free):
                1. gpt-4o
                2. gpt-4o-mini
                3. gpt-4-turbo
                4. gpt-3.5-turbo'''
                
= OpenAI(model="gpt-4o")



# ================================
#   DOCUMENT PARSING AND INDEXING
# ================================

parser = LlamaParse(
    os.environ["LLAMA_API_KEY"] = llama_api_key,
    result_type="markdown" # other options json, text, html, raw                                      
)
documents = await parser.aload_data(selected_file)
Print(f'Document {selected_file} correctly parsed')

index = VectorStoreIndex.from_documents(documents)
Print(f'Document {selected_file} correctly indexed')


query_engine = index.as_query_engine(
  index.as_query_engine(
    llm=select_model(),
    response_mode = "compact",
    include_text=True,  
    similarity_top_k=2,  
    verbose=True,
)
  
response = query_engine.query(user_query)
retrieved_nodes = response.source_nodes
retrieved_list = [node.text for node in retrieved_nodes]




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

# =====================
#   FILE SELECTION
# =====================

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Ottieni la chiave API di OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

# Imposta la chiave API nell'ambiente
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    print("API key loaded successfully.")
else:
    print("API key not found in .env file.")

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

# =====================
#   DOCUMENT PARSING
# =====================
             
parser = LlamaParse(
    # api_key="llx-oBMnoRgUcdtfgkyiFiDrKh5ka5IwUCqm3WlkfViw3TC8wNCA",  # chiave MARCO di https://cloud.llamaindex.ai/landing
    api_key="llx-x01ouaHuW4QSItmZFCo0ODxNe1MVw8PCYHg2U3YTSKtKbPaS",    # chiave FILIPPO di https://cloud.llamaindex.ai/landing
    result_type="markdown"                                             # altre opzioni: json, text, html, raw
)
documents = await parser.aload_data(selected_file)



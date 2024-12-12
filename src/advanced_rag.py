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

# - # - # - # - # - # - # - # - # - # - # -





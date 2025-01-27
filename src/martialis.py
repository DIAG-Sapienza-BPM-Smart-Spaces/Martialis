from llama_index.llms.mistralai import MistralAI # %pip install llama-index-llms-mistralai
from llama_index.core.llms import ChatMessage

from kg_automatic import kg_automatic
import sys


def main():

    # Parse input from command line if we need to use 
    # step 0 instead of the user input.
    if len(sys.argv) > 2:
        if sys.argv[1] == "step_0":
            step_0(sys.argv[2])

    
    user_prompt = input("Enter your prompt: ")
    response = modality_selection(user_prompt)

    if "advanced_rag" in response:
        advanced_rag()
    elif "ontology_validator" in response:
        ontology_validator()
    else:
        print("Invalid prompt")
        
def modality_selection(user_prompt):
    llm = MistralAI(model = "mistral-large-latest",
                    api_key="") 
    messages = [
        ChatMessage(role="system", 
                    content="""
                    Your task is to identify the user's requested task based on their prompt. You have two options:
                    1. "advanced_rag" for question answering;
                    2. "ontology_validator" for text generation.

                    Analyze the user's prompt and select one of the two options: "advanced_rag" or "ontology_validator". 

                    You must strictly return only "advanced_rag" or "ontology_validator" without adding any additional text or context."""),
        ChatMessage(role="user", content=user_prompt),
    ]
    resp = llm.chat(messages)
    return str(resp)

def advanced_rag():
    print("Advanced RAG function called")

def ontology_validator():
    print("Ontology Validator function called")

# Create a function called step 0 that call kg_automatic
def step_0(path):
    print(f"Step 0 function called. Parsing directory {path}")
    kg_automatic(path)
    

if __name__ == "__main__":
    main()

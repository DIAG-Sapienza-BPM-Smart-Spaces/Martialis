def main():
    user_prompt = input("Enter your prompt: ")
    parsed_prompt = parse_user_prompt(user_prompt)
    
    if parsed_prompt == "advanced_rag":
        advanced_rag()
    elif parsed_prompt == "ontology_validator":
        ontology_validator()
    else:
        print("Invalid prompt")

def parse_user_prompt(prompt):
    # Implement your parsing logic here
    return prompt.strip().lower()

def advanced_rag():
    print("Advanced RAG function called")

def ontology_validator():
    print("Ontology Validator function called")

# Create a function called step 0 that call kg_automatic
def step_0():
    print("Step 0 function called")

if __name__ == "__main__":
    main()
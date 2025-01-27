# prendi dal rispettivo notebook di marco
from llama_index.core import SimpleDirectoryReader
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from llama_index.core import PropertyGraphIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI





def parse_directory(directory_path, llm=OpenAI("gpt-4o"), embed_model=OpenAIEmbedding(model_name="text-embedding-3-small")):
    """
        Parse a directory of documents and create a property graph index.
    """

    documents = SimpleDirectoryReader(directory_path).load_data() # Add the path to the directory containing your documents here

    # Note: used to be `Neo4jPGStore`
    graph_store = Neo4jPropertyGraphStore(
        username="neo4j",
        password="insert_password",
        url="bolt://localhost:7687",
    )
    
    # create
    index = PropertyGraphIndex.from_documents(
        documents,
        llm=llm,
        embed_model=embed_model,
        property_graph_store=graph_store,
        show_progress=True,
    )

    return index
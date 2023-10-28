from sage import SageClient
from transformer import TransformerClient

if __name__ == "__main__":
    query = 'Hello, How are you?'
    sage_client = SageClient()
    response = sage_client.get_embeddings(query)

    # Uncommenting this will download model on local machine
    # trans_client = TransformerClient()
    # trans_client.get_embedding_vector(query)

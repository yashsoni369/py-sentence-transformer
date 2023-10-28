import torch
from typing import List
from sentence_transformers import SentenceTransformer, util


class TransformerClient:
    def __init__(self, model_name='all-mpnet-base-v2'):
        self.__model = SentenceTransformer(model_name)
        # To use CUDA install :
        # pip install torch==2.1.0+cu113 --index-url https://download.pytorch.org/whl/cu113
        self.__device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.__model.to(self.__device)

    @staticmethod
    def tensor_to_list(tensor):
        return tensor.detach().cpu().numpy().tolist()

    def list_to_tensor(self, embedding: List[float]):
        return torch.tensor(embedding).to(self.__device)

    def get_embedding_vector(self, content: str) -> List[float]:
        """
        Converts a given piece of text into an embedding vector.
        The embedding vector represents the text in an embedded space as a list of floats.

        :param content: The piece of text whose embedding vector has to be generated.
        :return: A list of floats representing the embedding vector.
        """
        # Normalizing the content by replacing \n by spaces
        content = content.replace("\n", " ")

        # Step I: If not present, then generate the embedding vector and store it in Redis.
        with torch.no_grad():
            query_embedding = self.__model.encode(content, convert_to_tensor=True)

            # OPTIONAL: Convert the tensor to a list.
            query_embedding = self.tensor_to_list(query_embedding)

            # Step II: Return the embedding vector.
        return [float(i) for i in query_embedding]

    def __compare_embeddings(self, embedding1: List[float], embedding2: List[float]) -> float:
        """
        Compares two embedding vectors and returns the similarity score.

        :param embedding1: The first embedding vector.
        :param embedding2: The second embedding vector.
        :return: The similarity score between the two embedding vectors.
        """
        # Step I: Convert the lists to tensors. (assuming all inputs will be Lists)
        embedding1 = self.list_to_tensor(embedding1)
        embedding2 = self.list_to_tensor(embedding2)

        # Step II: Compare the embeddings.
        cosine_score = util.pytorch_cos_sim(embedding1, embedding2)

        # Step III: Return the score.
        return cosine_score.item()
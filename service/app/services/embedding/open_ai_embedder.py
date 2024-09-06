import openai
import os
from typing import List
from app.config import OAIConfig
from app.services.embedding.embedder import Embedder
from app.logger import setup_logging

class OpenAIEmbedder(Embedder):
    """
    Embeddor class that uses OpenAI's API for generating embeddings.
    """

    logger = setup_logging("OpenAIEmbedder")
    source = "openai"

    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        Embeds the given text using OpenAI's API.

        Parameters:
        - text (str): The text to embed.

        Returns:
        - List[float]: The embedding of the given text.

        Note:
        - Requires the OpenAI API key to be set in the OAIConfig.api_key attribute.
        - The model used for embedding generation is specified in the OAIConfig.embed_model attribute.
        """
        OpenAIEmbedder.logger.info(f"Generating embedding for text.")

        # Retrieve the API key from environment or config
        api_key = OAIConfig.api_key or os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            raise ValueError("OpenAI API key is not set. Set it in OAIConfig.api_key or as an environment variable.")
        
        openai.api_key = api_key
        
        try:
            response = openai.Embedding.create(input=texts, model=OAIConfig.embed_model)
            embeddings = [v["embedding"] for v in response["data"]]                
            return embeddings
        except Exception as e:
            OpenAIEmbedder.logger.error(f"Error in generating embedding: {e}")
            raise

    def get_source(self) -> str:
        """
        Returns the source of the Embedder.

        Returns:
        - str: The source of the Embedder.
        """
        return OpenAIEmbedder.source
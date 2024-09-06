from app.logger import setup_logging
from app.config import EmbeddingConfig
from app.services.embedding.embedder import Embedder
from app.services.embedding.open_ai_embedder import OpenAIEmbedder

class EmbeddingService:
    """
    Service class to retrieve an Embedder based on a given source.
    """

    logger = setup_logging("EmbeddingService")

    embedder_classes = {
        "openai": OpenAIEmbedder,
        # Add new embeddor classes here as they become available
    }

    @staticmethod
    def get_embedder(embedding_source: str = EmbeddingConfig.default_source ) -> Embedder:
        """
        Returns an Embedder based on the given source.

        Parameters:
        - embedding_source (str): The source of the Embedder.

        Returns:
        - Embedder: An Embedder based on the given source.

        Raises:
        - ValueError: If the given source is not supported.
        """
        EmbeddingService.logger.info(f"Retrieving embedder for source: {embedding_source}")

        embedder_class = EmbeddingService.embedder_classes.get(embedding_source)
        if embedder_class:
            return embedder_class()
        else:
            raise ValueError(f"Unsupported Embedding source: {embedding_source}")

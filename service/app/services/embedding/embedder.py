from abc import ABC, abstractmethod
from typing import List

class Embedder(ABC):
    """
    Abstract class for an Embedder.
    """

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        Abstract method to embed a given text.

        Parameters:
        - texts (str): The texts to embed.

        Returns:
        - List[float]: The embedding of the given text.
        """
        pass

    def get_source(self) -> str:
        """
        Abstract method to get the source of the Embedder.

        Returns:
        - str: The source of the Embedder.
        """
        pass
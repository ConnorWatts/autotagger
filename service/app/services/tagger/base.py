from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Tagger(ABC):
    """
    Abstract base class for all taggers.
    """

    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize the tagger with an optional configuration.
        
        Parameters:
        - config (Dict[str, Any]): A dictionary of configuration options.
        """
        self.config = config or {}

    @abstractmethod
    def tag(self, text: str) -> List[str]:
        """
        Abstract method to tag a piece of text.

        Parameters:
        - text (str): The text to be tagged.

        Returns:
        - List[str]: A list of tags.
        """
        pass

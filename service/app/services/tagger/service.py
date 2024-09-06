from .llm import LLMTagger
from .hybrid import HybridTagger
from .similarity import SimilarityTagger
from typing import List, Dict, Any
from app.logger import setup_logging

class TaggerService:
    """
    Service for managing different types of taggers.
    """

    logger = setup_logging("TaggerService")

    @staticmethod
    def get_tagger(tagger_type: str, config: Dict[str, Any]):
        """
        Retrieves the appropriate tagger based on the provided tagger type.

        Parameters:
        - tagger_type (str): The type of tagger to retrieve ('agent', 'hybrid', 'similarity').
        - config (Dict[str, Any]): A dictionary of configuration options.

        Returns:
        - Tagger: The appropriate tagger class instance.
        """
        if tagger_type == "llm":
            return LLMTagger(config)
        elif tagger_type == "hybrid":
            return HybridTagger(config)
        elif tagger_type == "similarity":
            return SimilarityTagger(config)
        else:
            raise ValueError(f"Unknown tagger type: {tagger_type}")

    @staticmethod
    def tag_text(tagger_type: str, text: str, config: Dict[str, Any]) -> List[str]:
        """
        Tags a piece of text using the specified tagger type.

        Parameters:
        - tagger_type (str): The type of tagger to use ('agent', 'hybrid', 'similarity').
        - text (str): The text to be tagged.
        - config (Dict[str, Any]): A dictionary of configuration options.

        Returns:
        - List[str]: A list of tags.
        """
        tagger = TaggerService.get_tagger(tagger_type, config)
        return tagger.tag(text)

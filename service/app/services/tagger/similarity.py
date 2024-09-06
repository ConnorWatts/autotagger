from .base import Tagger
from typing import List

class SimilarityTagger(Tagger):
    """
    A tagger that uses similarity measures to tag text.
    """

    def __init__(self, config=None):
        super().__init__(config)
        self.similarity_metric = self.config.get("similarity_metric", "cosine")

    def tag(self, text: str) -> List[str]:
        # TODO: 
        return ...


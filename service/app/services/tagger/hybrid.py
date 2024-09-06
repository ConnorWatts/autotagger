from .base import Tagger
from typing import List

class HybridTagger(Tagger):
    """
    A tagger that uses a hybrid approach to tag text.
    """

    def __init__(self, config=None):
        super().__init__(config)
        self.hybrid_threshold = self.config.get("hybrid_threshold", 0.5)

    def tag(self, text: str) -> List[str]:
        # TODO:
        return ...

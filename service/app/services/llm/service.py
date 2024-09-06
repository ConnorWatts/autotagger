from typing import Dict, List

from app.services.llm.base import BaseLLM
from app.services.llm.openai import OpenAILLM
from app.logger import setup_logging

class LLMService:
    """
    LLMService class responsible for handling interactions with the Language Model (LLM).
    """

    logger = setup_logging("LLMService")

    @staticmethod
    def get_llm(model_config: Dict) -> BaseLLM:
        """
        Returns an instance of the Language Model.

        Parameters:
        - model (str, optional): Name of the specific model to be used.

        Returns:
        - LLM instance: An instance of the Language Model.

        Raises:
        - ValueError: If the LLM source is not supported.
        """
        source = model_config.get("model_source")
        if source == "openai":
            LLMService.logger.info(f"Retrieving LLM for source: {source}")
            return OpenAILLM(model_config)
        
        else:
            LLMService.logger.error(f"Unsupported LLM source: {source}")
            raise ValueError(f"Unsupported LLM source: {source}")
        
        # TODO: Extend this to more LLMs as they become available
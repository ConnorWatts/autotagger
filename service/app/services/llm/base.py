from abc import ABC, abstractmethod
from langchain.chains import LLMChain
import logging
from typing import Dict, Type
import langchain.prompts as prompts

class BaseLLM(ABC):
    def __init__(self):
        self.config = None
        self.llm = None

from .base import Tagger
from app.services.llm.service import LLMService
from app.services.prompt.service import PromptService
from app.services.category.service import CategoryService
from typing import List
import ast
import logging 

from app.logger import setup_logging

class LLMTagger(Tagger):
    """
    A tagger that uses an agent-based approach to tag text.
    """

    logger = setup_logging("LLMTagger")

    def __init__(self, config):
        super().__init__(config)
        self.tagging_config = config

        # llm stuff
        self.model_source = self.tagging_config.get("model_source") if "model_source" in self.tagging_config else "openai"
        self.model_name = self.tagging_config.get("model_name") if "model_name" in self.tagging_config else "gpt-4"
        self.llm = LLMService.get_llm({"model_source": self.model_source, "model_name": self.model_name})

        # tagging stuff
        self.takes = self.tagging_config.get("takes")
        self.k = self.tagging_config.get("k")
        self.categories = self.tagging_config.get("categories")
        self.recipe = self.tagging_config.get("recipe")

    def tag(self, text: str) -> List[str]:

        if self.takes == "one-take":
            return self.tag_one_take(text)
        
        if self.takes == "multi-take":
            return self.tag_multi_take(text)

    def tag_one_take(self, text: str) -> List[str]:
        prompt = PromptService.get_prompt_template(self.takes)
        prompt_out = prompt.prompt_template

        for input in prompt.prompt_input:

            if input == "k":
                prompt_out = prompt_out.replace("{k}", str(self.k))

            if input == "recipe":
                prompt_out = prompt_out.replace("{recipe}", self.recipe)

            if input == "category-tag":
                category_tags = CategoryService.get_category_tags_str(self.categories)
                prompt_out = prompt_out.replace("{category-tag}", category_tags)

        # Try 3 times 
        for i in range(3):
            try:
                response = self.llm.call(prompt_out)
                parsed_response = self.parse_dict_response(response)
                return parsed_response
            except Exception as e:
                self.logger.error(f"Error getting response from LLM Attempt {i}: {e}")
                continue

    def tag_multi_take(self, text: str) -> List[str]:

        out = {}
        prompt = PromptService.get_prompt_template(self.takes)

        for category in self.categories:
            prompt_out = prompt.prompt_template

            for input in prompt.prompt_input:

                if input == "k":
                    prompt_out = prompt_out.replace("{k}", str(self.k))

                if input == "recipe":
                    prompt_out = prompt_out.replace("{recipe}", self.recipe)

                if input == "tags":
                    category_tags = CategoryService.get_category_tags_str([category])
                    prompt_out = prompt_out.replace("{tags}", category_tags)

            # Try 3 times 
            for i in range(3):
                try:
                    response = self.llm.call(prompt_out)
                    parsed_response = self.parse_dict_response(response)
                    out.update(parsed_response)
                except Exception as e:
                    self.logger.error(f"Error getting response from LLM Attempt {i} for {category}: {e}")
                    continue

        return out
            

    
    def parse_dict_response(self, input_str: str) -> dict:
        """
        Parses a string representation of a dictionary into a Python dictionary.
        
        Parameters:
        - input_str (str): The string representation of the dictionary.
        
        Returns:
        - dict: The parsed dictionary.
        
        Raises:
        - ValueError: If the input string cannot be parsed as a dictionary.
        """
        # remove everything before the first '{' and after the last '}'
        input_str = input_str[input_str.find('{'):]
        input_str = input_str[:input_str.rfind('}') + 1]
        try:
            # Use ast.literal_eval for safely parsing the string into a Python object
            parsed_dict = ast.literal_eval(input_str)
            if isinstance(parsed_dict, dict):
                return parsed_dict
            else:
                raise ValueError("Input string is not a valid dictionary representation.")
        except (SyntaxError, ValueError) as e:
            raise ValueError(f"Error parsing string into dictionary: {e}")


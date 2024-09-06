from typing import Dict
from app.services.llm.base import BaseLLM
from app.config import OAIConfig
from openai import OpenAI

class OpenAILLM(BaseLLM):
    def __init__(self, model_config: Dict) -> None:
        super().__init__()
        self.model_name = model_config.get("model_name") if "model_name" in model_config else "gpt-4"
        self.llm_client = OpenAI(api_key=OAIConfig.api_key)

    def call(self, prompt: str) -> str:
        stream = self.llm_client.chat.completions.create(
        model=self.model_name,
        messages=[{"role": "user", "content": prompt}],
        )
        return stream.choices[0].message.content


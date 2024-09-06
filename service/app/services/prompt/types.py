from dataclasses import dataclass

@dataclass
class Prompt:
    prompt_template: str
    prompt_input: list

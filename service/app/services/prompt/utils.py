import re
from typing import List

def extract_text_within_braces(text: str) -> List[str]:
    """
    Extracts all substrings within curly braces from the given text.

    Parameters:
    - text (str): The input string.

    Returns:
    - List[str]: A list of all substrings found within curly braces.
    """
    # Use regex to find all instances of text within curly braces
    return re.findall(r'\{([^}]*)\}', text)

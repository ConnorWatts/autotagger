from app.services.prompt.types import Prompt
from app.services.prompt.utils import extract_text_within_braces

# TODO: Move all these prompts to a database (manage versioning accuracy etc)

one_take_prompt = """You are a culinary expert tasked with categorizing a recipe. Below is a recipe and a set of categories with their respective tags.

Your task is to return a JSON object where each category contains a list of the most relevant tags based on the recipe provided. Each category should have up to {k} relevant tags. If no tags from a category are relevant to the recipe, you can leave that category out of the JSON object.

Here is the recipe:
{recipe}

Here are the categories and their respective tags:
{category-tag}

Please return a JSON object in this format: {"category1": ["tag1", "tag2"], "category2": ["tag1"], ...} with the most relevant tags for the recipe. You can skip categories if they are not relevant.

---

**Small Example**:

Recipe: "A light apple salad with walnuts and honey, perfect for a starter."

Categories and Tags:
Ingredient: ["Apple", "Walnut", "Honey", "Lettuce", "Olive Oil"]
Dish Type: ["salad", "appetizer", "dessert"]
Meal Type: ["starter", "main course", "dessert"]
Occasion: ["lunch", "dinner", "brunch"]
Cuisine: ["american", "french", "italian"]
Dietary: ["vegetarian", "vegan", "gluten free", "dairy free"]

Example Expected JSON output:
{
  "Ingredient": ["Apple", "Walnut"],
  "Dish Type": ["salad"],
  "Meal Type": ["starter"],
  "Occasion": ["lunch"],
  "Cuisine": ["american"]
  "Dietary": ["vegetarian"]
}

Please just return the JSON object with the relevant tags for the recipe. Make sure you a through and consider everything that could be relevant. If possible return ALL categories, this is important.

---

Please return the JSON ONLY. Include ALL catgories and tags that are relevant to the recipe.

Now proceed to categorize the following recipe:"""

many_take_prompt = """You are a culinary expert tasked with categorizing a recipe. Below is a recipe and a set of tags in a category.

List of the most relevant tags based on the recipe provided. You should have up to {k} relevant tags. If no tags are relevant to the recipe, you can leave them out the final list.

Here is the recipe:
{recipe}

Here are the catgeory/tags:
{tags}

---

**Small Example**:

Recipe: "A light apple salad with starter."

Categories and Tags:
{"Ingredients": ["Apple", "Walnut", "Honey", "Lettuce", "Olive Oil"]}


Expected output:
{"Ingredients": ["Apple"]}

---

Please return just the output in the JSON format. Only that.

Now proceed to find the relevant tags from the following recipe:"""

class PromptService:

    @staticmethod
    def get_prompt_template(prompt_name:str) -> Prompt:
        """
        Retrieve a prompt by its name.

        Parameters:
        - prompt_name (str): The name of the prompt to retrieve.

        Returns:
        - Prompt: The Prompt object with the given name.
        """
        if prompt_name == "one-take":
            prompt_template = one_take_prompt
            inputs = extract_text_within_braces(prompt_template)
            return Prompt(one_take_prompt, inputs)
        
        if prompt_name == "multi-take":
            prompt_template = many_take_prompt
            inputs = extract_text_within_braces(prompt_template)
            return Prompt(many_take_prompt, inputs)
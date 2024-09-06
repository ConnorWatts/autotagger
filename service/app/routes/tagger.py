from flask import jsonify, request
from http import HTTPStatus
from logging import getLogger
from . import main
from app.services.tagger.service import TaggerService  

logger = getLogger(__name__)

from flask import Blueprint, render_template, request, jsonify
from app.services.tagger.service import TaggerService
from app.services.category.service import CategoryService

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/finetune', methods=['GET'])
def finetune():
    """
    Render the fine-tune page with mock data to simulate the tagging process.
    """
    # Simulate categories and tags fetched from API calls
    mock_tags = {
        "Ingredient": ["Pasta", "Tomato", "Olive Oil", "Garlic"],
        "Meal Type": ["Main Course", "Lunch", "Dinner"],
        "Cuisine": ["Italian", "Mediterranean"]
    }
    
    return render_template('finetune.html', mock_tags=mock_tags)

@main.route('/prompt_playground', methods=['GET'])
def prompt_playground():
    """
    Render the Prompt Playground page.
    """
    # Example prompt
    one_take_prompt = """You are a culinary expert tasked with categorizing a recipe..."""
    
    return render_template('prompt_playground.html', prompt_example=one_take_prompt)

@main.route("/api/tagger", methods=["POST"])
def tag_recipe():
    try:
        # Extract the request data from the form
        recipe = request.form.get("recipe")

        tagger_type = request.form.get("tagger_type", "llm")  # Defaulting to "llm"

        # Check if 'k' is empty or not provided and default to 2
        k = request.form.get("k")
        if not k or k == '':
            k = 2  # Default value for 'k'

        categories = request.form.get("categories")

        # Handle categories as a comma-separated string, if it's provided
        if categories:
            categories = [cat.strip() for cat in categories.split(",")]
        else:
            categories = CategoryService.get_all_unique_category_names()

        # Check if 'model_source' is empty or not provided and default to 'openai'
        model_source = request.form.get("model_source")
        if not model_source or model_source == '':
            model_source = "openai"  # Default value for 'model_source'

        # Check if 'model_name' is empty or not provided and default to 'gpt-4'
        model_name = request.form.get("model_name")
        if not model_name or model_name == '':
            model_name = "gpt-4"  # Default value for 'model_name'

        # Check if 'takes' is empty or not provided and default to 'multi-take'
        takes = request.form.get("takes")
        if not takes or takes == '':
            takes = "multi-take"  # Default value for 'takes'

        # Prepare tagging configuration
        tagging_config = {
            "model_source": model_source,  # Default to openai
            "model_name": model_name,  # Default to gpt-4
            "takes": takes,
            "k": k,
            "categories": categories,
            "recipe": recipe
        }

        # Call the TaggerService
        tags = TaggerService.tag_text(tagger_type, recipe, tagging_config)

        # Return the result
        return jsonify({"tags": tags}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

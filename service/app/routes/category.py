from flask import jsonify, request
from http import HTTPStatus
from logging import getLogger
from . import main
from app.services.category.service import CategoryService  # Assuming this is your service module

logger = getLogger(__name__)


@main.route("/api/categories", methods=["GET"])
def get_all_categories():
    """
    Get all categories.

    Returns:
        JSON: List of all categories if successful. Error message if failed.
    """
    try:
        categories = CategoryService.get_all_unique_category_names()
        return jsonify(categories), HTTPStatus.OK
    except Exception as e:
        logger.exception(f"Error retrieving categories: {str(e)}")
        return jsonify({"Error": "Failed to retrieve categories."}), HTTPStatus.INTERNAL_SERVER_ERROR


@main.route("/api/category/tags", methods=["GET"])
def get_tags_for_category():
    """
    Get all tags for a provided category.

    Query Params:
        category_id (int): The ID of the category for which tags are to be retrieved.

    Returns:
        JSON: List of tags for the category if successful. Error message if failed.
    """
    try:
        category_id = request.args.get("category_id")
        if not category_id:
            return jsonify({"Error": "category_id is required"}), HTTPStatus.BAD_REQUEST

        tags = CategoryService.get_tags_for_category(category_id)
        if tags is None:
            return jsonify({"Error": "Category not found"}), HTTPStatus.NOT_FOUND

        return jsonify(tags), HTTPStatus.OK
    except Exception as e:
        logger.exception(f"Error retrieving tags for category {category_id}: {str(e)}")
        return jsonify({"Error": "Failed to retrieve tags for the category."}), HTTPStatus.INTERNAL_SERVER_ERROR


@main.route("/api/category/tag", methods=["POST", "DELETE"])
def modify_category_tags():
    """
    Add or remove tags for a category.

    JSON Body (POST):
        category_id (int): The ID of the category.
        tag (str): The tag to be added.

    JSON Body (DELETE):
        category_id (int): The ID of the category.
        tag (str): The tag to be removed.

    Returns:
        JSON: Success message if the operation is successful, or error message if failed.
    """
    try:
        data = request.get_json()
        category_id = data.get("category_id")
        tag = data.get("tag")

        if not category_id or not tag:
            return jsonify({"Error": "category_id and tag are required"}), HTTPStatus.BAD_REQUEST

        if request.method == "POST":
            success = CategoryService.add_tag_to_category(category_id, tag)
            if success:
                return jsonify({"Message": f"Tag '{tag}' added to category {category_id}."}), HTTPStatus.OK
            else:
                return jsonify({"Error": "Failed to add tag to the category."}), HTTPStatus.BAD_REQUEST

        if request.method == "DELETE":
            success = CategoryService.remove_tag_from_category(category_id, tag)
            if success:
                return jsonify({"Message": f"Tag '{tag}' removed from category {category_id}."}), HTTPStatus.OK
            else:
                return jsonify({"Error": "Failed to remove tag from the category."}), HTTPStatus.BAD_REQUEST

    except Exception as e:
        logger.exception(f"Error modifying tags for category {category_id}: {str(e)}")
        return jsonify({"Error": "Failed to modify tags for the category."}), HTTPStatus.INTERNAL_SERVER_ERROR


@main.route("/api/category", methods=["POST", "DELETE"])
def modify_category():
    """
    Add or remove a category.

    JSON Body (POST):
        name (str): The name of the category to be added.

    JSON Body (DELETE):
        category_id (int): The ID of the category to be deleted.

    Returns:
        JSON: Success message if the operation is successful, or error message if failed.
    """
    try:
        data = request.get_json()

        if request.method == "POST":
            name = data.get("name")
            if not name:
                return jsonify({"Error": "Category name is required"}), HTTPStatus.BAD_REQUEST

            success = CategoryService.add_category(name)
            if success:
                return jsonify({"Message": f"Category '{name}' added successfully."}), HTTPStatus.CREATED
            else:
                return jsonify({"Error": "Failed to add category."}), HTTPStatus.BAD_REQUEST

        if request.method == "DELETE":
            category_id = data.get("category_id")
            if not category_id:
                return jsonify({"Error": "category_id is required"}), HTTPStatus.BAD_REQUEST

            success = CategoryService.remove_category(category_id)
            if success:
                return jsonify({"Message": f"Category {category_id} removed successfully."}), HTTPStatus.OK
            else:
                return jsonify({"Error": "Failed to remove category."}), HTTPStatus.BAD_REQUEST

    except Exception as e:
        logger.exception(f"Error modifying categories: {str(e)}")
        return jsonify({"Error": "Failed to modify the category."}), HTTPStatus.INTERNAL_SERVER_ERROR

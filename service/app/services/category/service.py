from app.models import Category, Categories
from app import db
from datetime import datetime
from typing import List
from app.logger import setup_logging
import json

class CategoriesService:
    """
    Service for handling operations on Default Categories objects.
    """

    logger = setup_logging("CategoriesService")

    @staticmethod
    def save_categories(categories: List[str]) -> Categories:
        """
        Save a new Categories object with a list of category names.

        Parameters:
        - categories (List[str]): List of category names to save.

        Returns:
        - Categories: The newly created Categories object.
        """
        # Create a new Categories object
        categories_collection = Categories(categories=categories, created_at=datetime.utcnow())
        db.session.add(categories_collection)
        db.session.commit()
        return categories_collection

    @staticmethod
    def get_most_recent_categories() -> Categories:
        """
        Retrieve the most recently created Categories object.

        Returns:
        - Categories: The most recently created Categories object.
        """
        return Categories.query.order_by(Categories.created_at.desc()).first()

    @staticmethod
    def update_categories(new_categories: List[str]) -> Categories:
        """
        Update the Categories collection by creating a new Categories object with the updated category list.
        The old Categories collection remains unchanged.

        Parameters:
        - new_categories (List[str]): The updated list of categories.

        Returns:
        - Categories: The newly created Categories object with the updated categories.
        """
        # Retrieve the most recent Categories object
        most_recent_categories = CategoriesService.get_most_recent_categories()

        if most_recent_categories is None:
            raise ValueError("No existing Categories object found to update.")

        # Combine new categories with the existing ones, ensuring no duplicates
        updated_categories = list(set(most_recent_categories.categories + new_categories))

        # Create a new Categories object with the updated list
        new_categories_collection = CategoriesService.save_categories(updated_categories)
        return new_categories_collection


class CategoryService:
    """
    Service for handling operations on individual Category objects.
    """

    logger = setup_logging("CategoryService")

    @staticmethod
    def category_exists(name: str) -> bool:
        """
        Check if a Category with the given name exists.

        Parameters:
        - name (str): The name of the category to check.

        Returns:
        - bool: True if the category exists, False otherwise.
        """
        category = Category.query.filter_by(name=name).first()
        return category is not None
    
    @staticmethod
    def get_all_unique_category_names() -> List[str]:
        """
        Retrieve all unique category names.

        Returns:
        - List[str]: List of all unique category names.
        """
        return list(set([category.name for category in Category.query.all()]))

    @staticmethod
    def create_category(name: str, tags: List[str]) -> Category:
        """
        Create a new Category with the given name and tags.

        Parameters:
        - name (str): The name of the category.
        - tags (List[dict]): List of tags to be associated with the category.

        Returns:
        - Category: The newly created Category object.

        Raises:
        - ValueError: If a Category with the given name already exists.
        """
        # Check if the category already exists
        if CategoryService.category_exists(name):
            raise ValueError(f"Category with name '{name}' already exists.")
        
        # Create a new category
        return CategoryService.save_category(name, tags)
        
    @staticmethod
    def save_category(name: str, tags: List[str]) -> Category:
        """
        Save a new Category with the given name and tags.

        Parameters:
        - name (str): The name of the category.
        - tags (List[dict]): List of tags to be associated with the category.

        Returns:
        - Category: The newly created Category object.
        """

        # Create a new category
        category = Category(name=name, tags=tags, created_at=datetime.utcnow())
        db.session.add(category)
        db.session.commit()
        return category
    

    @staticmethod
    def get_all_categories() -> List[Category]:
        """
        Retrieve all categories.

        Returns:
        - List[Category]: List of all categories.
        """
        return Category.query.all()
    
    @staticmethod
    def get_category_by_id(category_id: int) -> Category:
        """
        Retrieve a category by its ID.

        Parameters:
        - category_id (int): The ID of the category to retrieve.

        Returns:
        - Category: The Category object with the given ID.
        """
        return Category.query.get(category_id)
    
    @staticmethod
    def get_most_recent_category_by_name(name: str) -> Category:
        """
        Retrieve the most recently created category by its name.
        
        Parameters:
        - name (str): The name of the category to retrieve.
        
        Returns:
        - Category: The most recently created Category object with the given name.
        """
        return Category.query.filter_by(name=name).order_by(Category.created_at.desc()).first()
    
    @staticmethod
    def delete_category_by_id(category_id: int) -> bool:
        """
        Delete a category by its ID.

        Parameters:
        - category_id (int): The ID of the category to delete.

        Returns:
        - bool: True if the category was successfully deleted, False otherwise.
        """
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def add_tags_to_category(category_name: str, tags: List[str]) -> bool:
        """
        Add tags to a category.

        Parameters:
        - category_id (int): The ID of the category to add tags to.
        - tags (List[str]): List of tags to add to the category.

        Returns:
        - bool: True if the tags were successfully added, False otherwise.
        """
        category = CategoryService.get_most_recent_category_by_name(category_name)
        if not category:
            ValueError(f"Category with name '{category_name}' does not exist.")

        if category:
            tags = list(set(category.tags + tags))
            return CategoryService.save_category(category.name, tags)
        
        return False
    
    @staticmethod
    def get_category_tags_str(categories: str) -> str:
        out_ = {}
        for category in categories:
            category = CategoryService.get_most_recent_category_by_name(category)
            tags = category.tags
            out_[category.name] = tags
        return json.dumps(out_)
    
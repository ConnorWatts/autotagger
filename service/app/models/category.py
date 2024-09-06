from app import db
from pgvector.sqlalchemy import Vector
from datetime import datetime

class Categories(db.Model):
    """
    Represents a collection of Category objects.

    Attributes:
        id (int): Unique identifier for the collection of categories.
        created_at (datetime): The date and time when the category collection was created.
        categories (List[Category]): List of Category objects belonging to this collection.
    """
    
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with Category (one-to-many) categories = db.relationship("Category", backref="categories", lazy=True)
    categories = db.Column(db.JSON, nullable=True, default=list) 
 
    def __repr__(self):
        return f"<Categories(id={self.id}, created_at={self.created_at})>"

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "categories": [category.to_dict() for category in self.categories]
        }

class Category(db.Model):
    """
    Represents a category which can have multiple tags.

    Attributes:
        id (int): Unique identifier for the category.
        name (str): Name of the category.
        created_at (datetime): Date and time when the category was created.
        tags (List[Tag]): List of tags associated with the category.
    """

    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # TODO: Update this to use a proper relationship
    tags = db.Column(db.JSON, nullable=True, default=list) 

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name}, created_at={self.created_at})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "tags": [tag for tag in self.tags]  # List of tags associated with the category
        }


class Tag(db.Model):
    """
    Represents a tag associated with a category.

    Attributes:
        id (int): Unique identifier for the tag.
        category_id (int): Foreign key to the category.
        value (str): The name of the tag.
        embedding (Vector): Embedded vector for the tag (for potential search/embedding purposes).
        created_at (datetime): Date and time when the tag was created.
    """

    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)

    # Tag Information
    value = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # TODO: Update this to be embedding = db.Column(Vector(1536)) 
    embedding = db.Column(db.JSON, nullable=True)
    embedding_source = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Tag(id={self.id}, value={self.value})>"

    def to_dict(self):
        return {
            "id": self.id,
            "category_id": self.category_id,
            "value": self.value,
            "embedding": self.embedding,  # Ensure this is properly serialized when needed
            "created_at": self.created_at,
        }

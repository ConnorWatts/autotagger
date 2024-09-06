from app.models import Tag
from app import db
from sqlalchemy import desc
from app.logger import setup_logging

class TagService:
    logger = setup_logging("TagService")

    @staticmethod
    def create_tag(value: str, embedding: list, embedding_source: str) -> Tag:
        """Creates and saves a new tag."""
        TagService.logger.info(f"Creating tag with value: {value}, embedding_source: {embedding_source}")
        tag = Tag(value=value, embedding=embedding, embedding_source=embedding_source)
        db.session.add(tag)
        db.session.commit()
        TagService.logger.info(f"Tag created with ID: {tag.id}")
        return tag

    @staticmethod
    def get_most_recent_tag_by_value(value: str) -> Tag:
        """Retrieves the most recently created tag by its value (name)."""
        TagService.logger.info(f"Fetching most recent tag with value: {value}")
        tag = Tag.query.filter_by(value=value).order_by(desc(Tag.created_at)).first()
        if tag:
            TagService.logger.info(f"Most recent tag found with ID: {tag.id}")
        else:
            TagService.logger.warning(f"No tag found with value: {value}")
        return tag

    @staticmethod
    def get_tag_by_id(tag_id: int) -> Tag:
        """Retrieves a tag by its ID."""
        TagService.logger.info(f"Fetching tag by ID: {tag_id}")
        tag = Tag.query.get(tag_id)
        if tag:
            TagService.logger.info(f"Tag found with ID: {tag_id}")
        else:
            TagService.logger.warning(f"No tag found with ID: {tag_id}")
        return tag

    @staticmethod
    def delete_tag_by_id(tag_id: int) -> bool:
        """Deletes a tag by its ID."""
        TagService.logger.info(f"Attempting to delete tag with ID: {tag_id}")
        tag = Tag.query.get(tag_id)
        if tag:
            db.session.delete(tag)
            db.session.commit()
            TagService.logger.info(f"Tag with ID: {tag_id} deleted successfully")
            return True
        TagService.logger.warning(f"Tag with ID: {tag_id} not found, deletion failed")
        return False

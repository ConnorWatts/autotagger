from flask.cli import FlaskGroup
from app import create_app, db
from dotenv import load_dotenv

load_dotenv()

app = create_app("development")
cli = FlaskGroup(create_app=create_app)

@cli.command("create_db")
def create_db():
    # deletes db.models content
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()

if __name__ == "__main__":
    create_db()
    cli()
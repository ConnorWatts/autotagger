# AutoTagger

AutoTagger for recipes

---

### Prerequisites
- **Python 3.x** installed
- **Flask** and other dependencies listed in `requirements.txt`
- (Optional) **Docker** for containerized deployment

---

### Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Configuration

This is where I set up configuration for different environments. I configured the project for multiple environments (development, testing, production) in `config.py`. The configurations cover the database, model source, and any environment-specific settings required for running the application in Docker or locally.

For production, I used **Gunicorn** to serve the app, which helps with concurrency and scalability.

---

## Usage

### Running the Application

To run the application locally, I use the Flask development server:

```bash
flask run
```

## Once running

Visit `http://127.0.0.1:5000/` to access the main dashboard for the user.

### Features:

- **Multiple Tagging Strategies**:
  - **LLM Tagger**: Uses a large language model (LLM) like GPT to generate responses.
  - **Similarity Tagger**: (Not implemented yet) A lightweight, LLM-free approach based on vector similarity scoring.
  - **Hybrid Tagger**: (Not implemented yet) A combination of both LLM and similarity-based approaches to balance accuracy and performance.

- **Custom Configurations**:
  - Maximum number of tags per category (`k`).
  - Selection of relevant categories (e.g., ingredients, cuisine, meal type).
  - Choice of model source (e.g., OpenAI’s GPT).

You can visit `http://localhost:5000/api/docs/` to view the Swagger API documentation for the devs. 

---

## Extensions 

I ran out of time but these were some of the ideas I was working towards
  
- **Fine-Tuning**: 

http://127.0.0.1:5000/finetune A fine-tuning page where users can manually adjust tags suggested by the system. This would then go back and fine-tune the model.

- **Prompt Playground**

http://127.0.0.1:5000/prompt_playground A experimental prompting page where devs can test out new prompts.

- **Promts in DB**

I set up a PG to store the data (Categories, tags etc). The main motivation for this was to have dynamic lists that could be updated. The next step was to put the prompts on there as well but I didn't have time. This would have allowed for better versioning and storing metrics etc.

- **Similarity**: 

I stored embeddings with the tags with the goal of using some vector searches to take the load off the LLM. 

---

## Testing

I made a couple of tests but didn't manage to complete.

- To run the tests, use:
    ```bash
    pytest
    ```

or through docker-compose-test

---
## Flask Setup

I decided to develop this in **Flask** because I am most familiar with it. The project follows a classic Flask layout with the model definitions (database schema), route handlers (API logic), and main functionality (services) separated.

For production, I used **Gunicorn** as the WSGI server to handle concurrent requests and improve performance.

- **Routes**: The routes manage API endpoints for tagging and category management.
- **Services**: The core logic of the application, including interaction with the language model (LLM) and database, is encapsulated in services.
- **Models**: The database models (e.g., Tag, Category) represent the underlying data structure.

---

## TODO: 

The project has a lot of TODOs (I saw as less of an immediate priority).

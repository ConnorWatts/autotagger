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

IMPORTANT: To run this app you need the attached .env file (put in the same place as the .env.db)

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

As part of the tagging we only includ tags if they are relevant to the recipe. 

You can visit `http://localhost:5000/api/docs/` to view the Swagger API documentation for the devs. 

---

## Cloud Deployment

For cloud deployment, I would leverage **Docker** to containerize the application, making it easier to deploy across different environments. The steps would include:

1. **Dockerize the Application**: 
    - Build a Docker image containing the Flask app and its dependencies.
    - Use a multi-stage build to optimize the image size and ensure the final image is lightweight and secure.

2. **Choose a Cloud Provider**: 
    - I would likely use **AWS Elastic Beanstalk** for simplicity  and it's what I have experience with

3. **Database Setup**:
    - Use a managed service like **AWS RDS** or **GCP Cloud SQL** for Postgres, ensuring it is properly configured for production with automatic backups and failovers.

4. **Scaling**:
    - Auto-scaling can be configured in AWS to handle high traffic, scaling instances up or down based on demand.
    - **Load Balancer** in front of multiple app instances (handled by Elastic Beanstalk) to distribute incoming traffic evenly.

5. **Environment Variables**: 
    - Use secure mechanisms like AWS Secrets Manager for environment variables such as API keys. It's currently just in an .env file. 

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

or through docker-compose-test. 

## LLM Alignment 

Several approaches can be taken do get better accuracy:
  
- **Human Feedback**: Collect feedback on tag relevance from real users, storing results to evaluate and fine-tune the system.
      
- **LLM Judge**: Use another LLM (or the same) to judge the quality of generated tags by comparing the tags to ground truth tags or evaluating based on context.
      
- **Metrics**: Key metrics for evaluating LLM outputs include:
    - **Relevance**: How closely the tag matches the recipe's content.
    - **Coverage**: Ensuring that each category (e.g., Ingredient, Cuisine) is tagged appropriately.
    - **Accuracy**: Confirm that the tags adhere to the predefined list of allowable tags and do not exceed `k` per category.


---
## Flask Setup

I decided to develop this in **Flask** because I am most familiar with it. The project follows a classic Flask layout with the model definitions (database schema), route handlers (API logic), and main functionality (services) separated.

For production, I used **Gunicorn** as the WSGI server to handle concurrent requests and improve performance.

- **Routes**: The routes manage API endpoints for tagging and category management.
- **Services**: The core logic of the application, including interaction with the language model (LLM) and database, is encapsulated in services.
- **Models**: The database models (e.g., Tag, Category) represent the underlying data structure.

---


## Limitations

- **Tag Relevance**: Although the system uses an LLM to generate tags, it sometimes struggles to consistently identify the most relevant tags for each category

## TODO: 

The project has a lot of TODOs (I saw as less of an immediate priority).

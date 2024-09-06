import unittest
import sys
import os
from app import create_app 

class TaggerRoutesTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = create_app('testing')  # Assuming 'testing' is your Flask config for testing
        self.client = self.app.test_client()

    def test_tag_recipe(self):
        # Test the tag recipe route
        data = {
            "recipe": "Pasta with tomato sauce",
            "tagger_type": "llm",
            "k": 2,
            "categories": "Ingredient, Meal Type",
            "model_source": "openai",
            "model_name": "gpt-4",
            "takes": "one-take"
        }
        
        response = self.client.post('/api/tagger', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('tags', response.json)
        print("Generated Tags:", response.json['tags'])

    def test_tag_recipe_missing_data(self):
        # Test missing recipe data
        response = self.client.post('/api/tagger', data={})
        self.assertEqual(response.status_code, 500)
        print("Error response:", response.json)

if __name__ == '__main__':
    unittest.main()
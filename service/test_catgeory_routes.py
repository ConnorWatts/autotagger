import unittest
from unittest.mock import patch
from app import create_app

# TODO: Create mock test for all routes

class CategoryRoutesTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_get_all_categories(self, mock_get_all_unique_category_names):

        # DEMONSTRATE: FAILING TEST
        mock_get_all_unique_category_names.return_value = ["Ingredient", "Meal Type"]

        # Test the GET /api/categories route
        response = self.client.get('/api/categories')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ["Ingredient", "Meal Type"])

if __name__ == '__main__':
    unittest.main()

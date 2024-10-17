import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000'

class TestDatabaseClient(unittest.TestCase):

    def setUp(self):
        url = f'{BASE_URL}/create_table'
        data = {"table_name": "test_table"}
        requests.post(url, json=data)

    def test_create_table(self):
        url = f'{BASE_URL}/create_table'
        data = {"table_name": "test_table"}
        response = requests.post(url, json=data)
        if response.status_code == 400:
            self.assertIn("Table 'test_table' already exists", response.json()['error'])
        else:
            self.assertEqual(response.status_code, 200)
            self.assertIn("Table 'test_table' created successfully", response.json()['message'])


    def test_insert_row(self):
        url = f'{BASE_URL}/insert_row'
        row_data = ["John Doe", 30, "file1.txt", 85.6, "J"]
        data = {
            "table_name": "test_table",
            "row_data": row_data
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Row", response.json()['message'])

    def test_search_row(self):
        url = f'{BASE_URL}/search_row'
        params = {
            "table_name": "test_table",
            "pattern": "John"
        }
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIn("John Doe", str(response.json()['search_results']))

    def test_get_rows(self):
        url = f'{BASE_URL}/insert_row'
        row_data = ["John Doe", 30, "file1.txt", 85.6, "J"]
        requests.post(url, json={
            "table_name": "test_table",
            "row_data": row_data
        })

        url = f'{BASE_URL}/get_rows'
        params = {"table_name": "test_table"}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIn("John Doe", str(response.json()['rows']))

    def test_update_row(self):
        url = f'{BASE_URL}/update_row'
        new_row_data = ["Jane Doe", 28, "file2.txt", 90.0, "J"]
        data = {
            "table_name": "test_table",
            "row_index": 0,  
            "new_row_data": new_row_data
        }
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Row 0 updated successfully", response.json()['message'])

    def test_delete_table(self):
        url = f'{BASE_URL}/delete_table'
        data = {"table_name": "test_table"}
        response = requests.delete(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Table 'test_table' deleted successfully", response.json()['message'])

    def test_save_database(self):
        url = f'{BASE_URL}/save_database'
        response = requests.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Database saved successfully", response.json()['message'])

    def test_load_database(self):
        url = f'{BASE_URL}/save_database'
        response = requests.post(url)
        self.assertEqual(response.status_code, 200)
        
        url = f'{BASE_URL}/load_database'
        response = requests.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Database loaded successfully", response.json()['message'])



if __name__ == '__main__':
    unittest.main()

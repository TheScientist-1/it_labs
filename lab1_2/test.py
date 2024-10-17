import unittest
from database import Database
from schema import Schema

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.schema = Schema({
            'name': 'string',
            'age': 'integerInvl',  
            'file': 'text_file',   
            'score': 'real',      
            'initial': 'char'      
        })
        self.db = Database()
        self.db.create_table('people', self.schema)

    def test_create_table(self):
        print("Running test_create_table...")
        self.assertIn('people', self.db.tables)
        self.assertEqual(len(self.db.tables['people'].rows), 0)

    def test_insert_valid_row(self):
        print("Running test_insert_valid_row...")
        self.db.tables['people'].insert_row(['John', 30, 'file1.txt', 85.6, 'J'])
        self.assertEqual(len(self.db.tables['people'].rows), 1)
        self.assertEqual(self.db.tables['people'].rows[0].data, ['John', 30, 'file1.txt', 85.6, 'J'])

    def test_insert_invalid_integerInvl(self):
        print("Running test_insert_invalid_integerInvl...")
        with self.assertRaises(Exception) as context:
            self.db.tables['people'].insert_row(['Jane', 1500, 'file2.txt', 90.2, 'J'])
        self.assertTrue('Invalid data type for field age' in str(context.exception))
        print("Passed invalid integerInvl test.")

    def test_insert_invalid_text_file(self):
        print("Running test_insert_invalid_text_file...")
        with self.assertRaises(Exception) as context:
            self.db.tables['people'].insert_row(['Jane', 25, 12345, 90.2, 'J']) 
        self.assertTrue('Invalid data type for field file' in str(context.exception))
        print("Passed invalid text_file test.")

    def test_search_by_name(self):
        print("Running test_search_by_name...")
        self.db.tables['people'].insert_row(['John', 30, 'file1.txt', 85.6, 'J'])
        self.db.tables['people'].insert_row(['Jane', 25, 'file2.txt', 90.2, 'J'])
        result = self.db.tables['people'].search('name', 'Jane')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], ['Jane', 25, 'file2.txt', 90.2, 'J'])

    def test_save_and_load_database(self):
        print("Running test_save_and_load_database...")
        self.db.tables['people'].insert_row(['John', 30, 'file1.txt', 85.6, 'J'])
        self.db.save_to_disk('test_database.json')

        new_db = Database()
        new_db.load_from_disk('test_database.json')

        self.assertIn('people', new_db.tables)
        self.assertEqual(len(new_db.tables['people'].rows), 1)
        self.assertEqual(new_db.tables['people'].rows[0].data, ['John', 30, 'file1.txt', 85.6, 'J'])

if __name__ == '__main__':
    unittest.main()

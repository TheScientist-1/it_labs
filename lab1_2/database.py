import json
from table import Table
from schema import Schema

class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, schema):
        """
        Створює таблицю з вказаною назвою і схемою.
        """
        if table_name in self.tables:
            raise Exception(f"Table {table_name} already exists.")
        self.tables[table_name] = Table(schema)
        print(f"Table '{table_name}' created.")

    def drop_table(self, table_name):
        """
        Видаляє таблицю з бази.
        """
        if table_name in self.tables:
            del self.tables[table_name]
            print(f"Table '{table_name}' dropped.")
        else:
            raise Exception(f"Table {table_name} does not exist.")

    def save_to_disk(self, file_path):
        """
        Зберігає всі таблиці в файл у форматі JSON.
        """
        data = {}
        for table_name, table in self.tables.items():
            data[table_name] = {
                'schema': table.schema.fields,
                'rows': [row.data for row in table.rows]
            }
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Database saved to {file_path}.")

    def load_from_disk(self, file_path):
        """
        Завантажує базу даних із файлу у форматі JSON.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Відновлення таблиць та рядків
                for table_name, table_data in data.items():
                    schema = Schema(table_data['schema'])
                    table = Table(schema)
                    for row_data in table_data['rows']:
                        table.insert_row(row_data)
                    self.tables[table_name] = table
            print(f"Database loaded from {file_path}.")
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error loading database: {e}")

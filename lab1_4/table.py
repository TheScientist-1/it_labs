from row import Row
from schema import Schema

class Table:
    def __init__(self, schema):
        """
        Ініціалізація таблиці з заданою схемою.
        schema: екземпляр класу Schema, який визначає поля таблиці
        """
        self.schema = schema
        self.rows = []

    def insert_row(self, data):
        """
        Додає новий рядок у таблицю після валідації даних.
        data: список значень, які відповідають полям схеми
        """
        if len(data) != len(self.schema.fields):
            raise Exception("Data length does not match schema length.")
        
        row = Row(data)
        
        row.validate_row(self.schema)
        
        self.rows.append(row)
        print(f"Row {data} inserted into table.")

    def delete_row(self, row_index):
        """
        Видаляє рядок з таблиці за індексом.
        row_index: індекс рядка, який потрібно видалити
        """
        if row_index < 0 or row_index >= len(self.rows):
            raise Exception("Invalid row index.")
        self.rows.pop(row_index)
        print(f"Row at index {row_index} deleted from table.")

    def update_row(self, row_index, new_data):
        """
        Оновлює дані рядка в таблиці.
        row_index: індекс рядка для оновлення
        new_data: нові дані, які замінять існуючі
        """
        if len(new_data) != len(self.schema.fields):
            raise Exception("Data length does not match schema length.")
        if row_index < 0 or row_index >= len(self.rows):
            raise Exception("Invalid row index.")
        
        self.rows[row_index].edit_row(new_data)
        self.rows[row_index].validate_row(self.schema)
        print(f"Row at index {row_index} updated to {new_data}.")
    
    def get_rows(self):
        """
        Повертає всі рядки в таблиці.
        """
        return [row.data for row in self.rows]

    def __repr__(self):
        """
        Повертає текстове представлення таблиці (для зручності).
        """
        return f"Table(schema={self.schema.fields}, rows={self.get_rows()})"
    
    def search(self, field_name, pattern):
        """
        Пошук рядків за шаблоном у певному полі таблиці.
        field_name: назва поля для пошуку
        pattern: шаблон для пошуку (наприклад, частковий збіг рядка)
        """
        field_index = list(self.schema.fields.keys()).index(field_name)
        found_rows = []

        for row in self.rows:
            if pattern in str(row.data[field_index]):
                found_rows.append(row.data)

        return found_rows
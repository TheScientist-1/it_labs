class Row:
    def __init__(self, data):
        """
        Ініціалізує рядок з переданими даними.
        data: список значень, які відповідають полям таблиці
        """
        self.data = data

    def edit_row(self, new_data):
        """
        Оновлює дані рядка новими значеннями.
        new_data: список нових значень для оновлення
        """
        self.data = new_data

    def validate_row(self, schema):
        """
        Перевіряє відповідність даних у рядку зі схемою таблиці.
        schema: об'єкт класу Schema, який містить інформацію про поля і їх типи
        """
        for i, (value, field_type) in enumerate(zip(self.data, schema.fields.values())):
            if not self._validate_type(value, field_type):
                raise Exception(f"Invalid data type for field {list(schema.fields.keys())[i]}: Expected {field_type}, got {type(value).__name__}")

    def _validate_type(self, value, field_type):
        """
        Приватний метод для перевірки відповідності типу даних до типу, визначеного у схемі.
        """
        if field_type == 'integer':
            return isinstance(value, int)
        elif field_type == 'real':
            return isinstance(value, float)
        elif field_type == 'char':
            return isinstance(value, str) and len(value) == 1
        elif field_type == 'string':
            return isinstance(value, str)
        elif field_type == 'integerInvl':
            return isinstance(value, int) and 0 <= value <= 1000
        elif field_type == 'text_file':
            return isinstance(value, str)
        else:
            raise Exception(f"Unknown field type: {field_type}")

    def __repr__(self):
        """
        Повертає текстове представлення рядка (для зручності).
        """
        return f"Row(data={self.data})"

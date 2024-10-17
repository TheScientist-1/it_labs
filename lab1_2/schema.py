class Schema:
    def __init__(self, fields):
        """
        Ініціалізує схему таблиці.
        fields: словник, який містить назви полів як ключі та типи полів як значення
        """
        self.fields = fields

    def validate(self, data):
        """
        Перевіряє відповідність переданих даних типам, визначеним у схемі.
        data: список значень, які відповідають полям таблиці
        """
        if len(data) != len(self.fields):
            raise Exception("Data length does not match schema length.")
        
        for i, (value, field_type) in enumerate(zip(data, self.fields.values())):
            if not self._validate_type(value, field_type):
                raise Exception(f"Invalid data type for field {list(self.fields.keys())[i]}: Expected {field_type}, got {type(value).__name__}")
        
        print("Data is valid according to the schema.")
    
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
        Повертає текстове представлення схеми (для зручності).
        """
        return f"Schema(fields={self.fields})"

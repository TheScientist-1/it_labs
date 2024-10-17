from database import Database
from schema import Schema

def main():
    db = Database()

    person_schema = Schema({
        'name': 'string',
        'age': 'integerInvl', 
        'file': 'text_file',  
        'score': 'real',       
        'initial': 'char'      
    })

    db.create_table('people', person_schema)

    db.tables['people'].insert_row(['John', 30, 'file1.txt', 85.6, 'J'])
    db.tables['people'].insert_row(['Jane', 25, 'file2.txt', 90.2, 'J'])

    found_rows = db.tables['people'].search('name', 'Jane')
    print("Found rows:", found_rows)

    db.save_to_disk('database.json')

    db.load_from_disk('database.json')

    print("Rows after loading from disk:")
    for row in db.tables['people'].get_rows():
        print(row)

if __name__ == "__main__":
    main()

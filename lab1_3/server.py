from flask import Flask, request, jsonify
from database import Database
from schema import Schema
import os

app = Flask(__name__)

db = Database()

@app.route('/create_table', methods=['POST'])
def create_table():
    data = request.json
    table_name = data.get('table_name')
    if table_name in db.tables:
        return jsonify({'error': f"Table '{table_name}' already exists."}), 400
    
    schema = Schema({
        'name': 'string',
        'age': 'integerInvl',
        'file': 'text_file',
        'score': 'real',
        'initial': 'char'
    })
    db.create_table(table_name, schema)
    return jsonify({'message': f"Table '{table_name}' created successfully."})


@app.route('/insert_row', methods=['POST'])
def insert_row():
    data = request.json
    table_name = data.get('table_name')
    row_data = data.get('row_data')  
    
    try:
        db.tables[table_name].insert_row(row_data)
        return jsonify({'message': f"Row {row_data} inserted into table '{table_name}' successfully."})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/search_row', methods=['GET'])
def search_row():
    table_name = request.args.get('table_name')
    search_pattern = request.args.get('pattern')
    
    try:
        result = db.tables[table_name].search('name', search_pattern)
        return jsonify({'search_results': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_rows', methods=['GET'])
def get_rows():
    table_name = request.args.get('table_name')
    
    try:
        rows = db.tables[table_name].get_rows()
        return jsonify({'rows': rows})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

@app.route('/delete_table', methods=['DELETE'])
def delete_table():
    data = request.json
    table_name = data.get('table_name')
    
    if table_name in db.tables:
        del db.tables[table_name]
        return jsonify({'message': f"Table '{table_name}' deleted successfully."})
    else:
        return jsonify({'error': f"Table '{table_name}' not found."}), 404

@app.route('/update_row', methods=['PUT'])
def update_row():
    data = request.json
    table_name = data.get('table_name')
    row_index = data.get('row_index') 
    new_row_data = data.get('new_row_data')
    
    try:
        db.tables[table_name].rows[row_index].data = new_row_data
        return jsonify({'message': f"Row {row_index} updated successfully."})
    except IndexError:
        return jsonify({'error': 'Row not found.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

import json

@app.route('/save_database', methods=['POST'])
def save_database():
    file_path = 'database.json' 
    try:
        with open(file_path, 'w') as f:
            json.dump({table_name: [row.data for row in table.rows] for table_name, table in db.tables.items()}, f)
        return jsonify({'message': 'Database saved successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/load_database', methods=['POST'])
def load_database():
    file_path = 'database.json'  
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for table_name, rows in data.items():
                if table_name not in db.tables:
                    schema = Schema({
                        'name': 'string',
                        'age': 'integerInvl',
                        'file': 'text_file',
                        'score': 'real',
                        'initial': 'char'
                    }) 
                    db.create_table(table_name, schema)
                for row_data in rows:
                    db.tables[table_name].insert_row(row_data)
        return jsonify({'message': 'Database loaded successfully.'})
    except FileNotFoundError:
        return jsonify({'error': 'Database file not found.'}), 404
    except Exception as e:
        return jsonify({'error': f"Error during loading database: {str(e)}"}), 500



if __name__ == '__main__':
    app.run(debug=True)

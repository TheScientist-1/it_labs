import requests

BASE_URL = 'http://127.0.0.1:5000'

def create_table(table_name):
    url = f'{BASE_URL}/create_table'
    data = {"table_name": table_name}
    response = requests.post(url, json=data)
    print(response.json())

def insert_row(table_name, row_data):
    url = f'{BASE_URL}/insert_row'
    data = {
        "table_name": table_name,
        "row_data": row_data
    }
    response = requests.post(url, json=data)
    print(response.json())

def search_row(table_name, pattern):
    url = f'{BASE_URL}/search_row'
    params = {
        "table_name": table_name,
        "pattern": pattern
    }
    response = requests.get(url, params=params)
    print(response.json())

def get_rows(table_name):
    url = f'{BASE_URL}/get_rows'
    params = {
        "table_name": table_name
    }
    response = requests.get(url, params=params)
    print(response.json())

def delete_table(table_name):
    url = f'{BASE_URL}/delete_table'
    data = {"table_name": table_name}
    response = requests.delete(url, json=data)
    print(response.json())

def update_row(table_name, row_index, new_row_data):
    url = f'{BASE_URL}/update_row'
    data = {
        "table_name": table_name,
        "row_index": row_index,
        "new_row_data": new_row_data
    }
    response = requests.put(url, json=data)
    print(response.json())

def save_database():
    url = f'{BASE_URL}/save_database'
    response = requests.post(url)
    print(response.json())

def load_database():
    url = f'{BASE_URL}/load_database'
    response = requests.post(url)
    print(response.json())

def delete_table(table_name):
    url = f'{BASE_URL}/delete_table'
    data = {"table_name": table_name}
    response = requests.delete(url, json=data)
    print(response.json())

def update_row(table_name, row_index, new_row_data):
    url = f'{BASE_URL}/update_row'
    data = {
        "table_name": table_name,
        "row_index": row_index,
        "new_row_data": new_row_data
    }
    response = requests.put(url, json=data)
    print(response.json())

def save_database():
    url = f'{BASE_URL}/save_database'
    response = requests.post(url)
    print(response.json())

def load_database():
    url = f'{BASE_URL}/load_database'
    response = requests.post(url)
    print(response.json())




import tkinter as tk
from tkinter import messagebox
from database import Database 
from schema import Schema     

class DatabaseApp:
    def __init__(self, root):
        self.db = Database()  
        self.root = root
        self.root.title("Database Management System")
        
        self.label_title = tk.Label(root, text="Database Management System", font=("Arial", 16))
        self.label_title.pack(pady=10)

        self.label_table_name = tk.Label(root, text="Table Name:")
        self.label_table_name.pack()

        self.entry_table_name = tk.Entry(root)
        self.entry_table_name.pack()

        self.label_row_data = tk.Label(root, text="Insert Row (comma separated):")
        self.label_row_data.pack()

        self.entry_row_data = tk.Entry(root)
        self.entry_row_data.pack()

        self.button_create_table = tk.Button(root, text="Create Table", command=self.create_table)
        self.button_create_table.pack(pady=5)

        self.button_insert_row = tk.Button(root, text="Insert Row", command=self.insert_row)
        self.button_insert_row.pack(pady=5)

        self.button_search = tk.Button(root, text="Search by Name", command=self.search_row)
        self.button_search.pack(pady=5)

        self.label_search_pattern = tk.Label(root, text="Search Pattern:")
        self.label_search_pattern.pack()

        self.entry_search_pattern = tk.Entry(root)
        self.entry_search_pattern.pack()

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack(pady=10)

    def create_table(self):
        table_name = self.entry_table_name.get()
        if not table_name:
            messagebox.showerror("Error", "Please enter a table name")
            return

        schema = Schema({
            'name': 'string',
            'age': 'integerInvl',
            'file': 'text_file',
            'score': 'real',
            'initial': 'char'
        })
        
        self.db.create_table(table_name, schema)
        messagebox.showinfo("Success", f"Table '{table_name}' created!")

    def insert_row(self):
        table_name = self.entry_table_name.get()
        row_data_str = self.entry_row_data.get()

        if not table_name or not row_data_str:
            messagebox.showerror("Error", "Please enter both table name and row data")
            return

        try:
            row_data = [val.strip() for val in row_data_str.split(",")]
            
            row_data[1] = int(row_data[1]) 
            row_data[3] = float(row_data[3]) 
            
            self.db.tables[table_name].insert_row(row_data)
            messagebox.showinfo("Success", f"Row {row_data} inserted into table '{table_name}'")
            self.show_all_rows(table_name)
        except ValueError:
            messagebox.showerror("Error", "Invalid data type. Ensure that age is an integer and score is a float.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def search_row(self):
        table_name = self.entry_table_name.get()
        search_pattern = self.entry_search_pattern.get()

        if not table_name or not search_pattern:
            messagebox.showerror("Error", "Please enter both table name and search pattern")
            return

        try:
            result = self.db.tables[table_name].search('name', search_pattern)
            self.text_output.delete(1.0, tk.END)
            self.text_output.insert(tk.END, f"Search Results for '{search_pattern}':\n")
            for row in result:
                self.text_output.insert(tk.END, f"{row}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_all_rows(self, table_name):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, f"All Rows in '{table_name}':\n")
        for row in self.db.tables[table_name].get_rows():
            self.text_output.insert(tk.END, f"{row}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

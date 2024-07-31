import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

# Create the main window
root = tk.Tk()
root.title("Student Registration")

# Connect to MongoDB
client = MongoClient()
db = client.students_db
collection = db.students

# Function to get the next ID
def get_next_id():
    last_student = collection.find_one(sort=[("id", -1)])
    if last_student:
        return last_student["id"] + 1
    else:
        return 1

# Function to save student data
def add_student():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    student_id = get_next_id()

    student_data = {
        'id': student_id,
        'name': name,
        'email': email,
        'age': age
    }

    collection.insert_one(student_data)

    # Refresh the table to show the new student
    refresh_table()

    # Clear the input fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Function to find a student by name
def find_student():
    name = entry_name.get()
    student = collection.find_one({'name': name})
    table.delete(*table.get_children())  # Clear the table
    if student:
        table.insert("", tk.END, values=(student['id'], student['name'], student['email'], student['age']))
    else:
        print("Student not found")

# Function to delete a student by name
def delete_student():
    name = entry_name.get()
    result = collection.delete_one({'name': name})
    if result.deleted_count > 0:
        print(f"Deleted student: {name}")
        refresh_table()
    else:
        print("Student not found")

# Function to order students by a field
def order_students():
    field = combo_order.get()
    students = collection.find().sort(field)
    table.delete(*table.get_children())  # Clear the table
    for student in students:
        table.insert("", tk.END, values=(student['id'], student['name'], student['email'], student['age']))

# Function to refresh the table
def refresh_table():
    students = collection.find().sort("id", 1)
    table.delete(*table.get_children())  # Clear the table
    for student in students:
        table.insert("", tk.END, values=(student['id'], student['name'], student['email'], student['age']))

# Create Frames for better layout
frame_inputs = tk.Frame(root, padx=10, pady=10)
frame_inputs.pack(side=tk.TOP, fill=tk.X)

frame_buttons = tk.Frame(root, padx=10, pady=10)
frame_buttons.pack(side=tk.TOP, fill=tk.X)

frame_table = tk.Frame(root, padx=10, pady=10)
frame_table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Creating input fields
label_name = tk.Label(frame_inputs, text='Name')
label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_name = tk.Entry(frame_inputs)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_email = tk.Label(frame_inputs, text='Email')
label_email.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_email = tk.Entry(frame_inputs)
entry_email.grid(row=1, column=1, padx=5, pady=5)

label_age = tk.Label(frame_inputs, text='Age')
label_age.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_age = tk.Entry(frame_inputs)
entry_age.grid(row=2, column=1, padx=5, pady=5)

# Creating buttons
button_save = tk.Button(frame_buttons, text='Add', command=add_student)
button_save.grid(row=0, column=0, padx=5, pady=5)

button_find = tk.Button(frame_buttons, text='Find', command=find_student)
button_find.grid(row=0, column=1, padx=5, pady=5)

button_delete = tk.Button(frame_buttons, text='Delete', command=delete_student)
button_delete.grid(row=0, column=2, padx=5, pady=5)

# Creating a dropdown menu for ordering
combo_order = ttk.Combobox(frame_buttons, values=['name', 'email', 'age'])
combo_order.grid(row=0, column=3, padx=5, pady=5)
button_order = tk.Button(frame_buttons, text='Order', command=order_students)
button_order.grid(row=0, column=4, padx=5, pady=5)

# Creating table Treeview
table = ttk.Treeview(frame_table, columns=('ID', 'Name', 'Email', 'Age'), show='headings')
table.heading('ID', text='ID')
table.heading('Name', text='Name')
table.heading('Email', text='Email')
table.heading('Age', text='Age')
table.pack(fill=tk.BOTH, expand=True)

# Initial population of the table
refresh_table()

root.mainloop()

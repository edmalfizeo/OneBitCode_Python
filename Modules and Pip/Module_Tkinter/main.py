import tkinter as tk

# Building the main window
window = tk.Tk()
window.geometry("400x400")
window.title("Phrase Manager")

# Adding a Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# Adding a Label
label = tk.Label(frame, text="Hello World!")
label.pack(fill='x', expand=True)

# Adding a Input
Phrase_label = tk.Label(frame, text="Enter a Phrase:")
Phrase_label.pack(fill='x', expand=True)

Phrase_entry = tk.Entry(frame)
Phrase_entry.pack(fill='x', expand=True)


# Function for changing the Text
def change_text():
    label.config(text=Phrase_entry.get())


# Adding a Button
button = tk.Button(frame, text="Submit", command=change_text)
button.pack()

window.mainloop()


import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#f7f7f7")

        # List to store tasks
        self.tasks = []

        # Title Label
        tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f7f7f7").pack(pady=10)

        # Task Display (Listbox)
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 14), selectmode=tk.SINGLE, bg="#fff", fg="#333")
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Input Field and Add Button
        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(fill=tk.X, padx=20, pady=5)
        tk.Button(root, text="Add Task", command=self.add_task, bg="#4caf50", fg="#fff", font=("Helvetica", 12)).pack(pady=5)

        # Action Buttons
        action_frame = tk.Frame(root, bg="#f7f7f7")
        action_frame.pack(pady=10)
        tk.Button(action_frame, text="Mark as Complete", command=self.mark_complete, bg="#ff9800", fg="#fff", font=("Helvetica", 12)).grid(row=0, column=0, padx=5)
        tk.Button(action_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="#fff", font=("Helvetica", 12)).grid(row=0, column=1, padx=5)
        tk.Button(action_frame, text="Clear All", command=self.clear_tasks, bg="#9e9e9e", fg="#fff", font=("Helvetica", 12)).grid(row=0, column=2, padx=5)

        # Menu for Save/Load
        menu = tk.Menu(root)
        root.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save Tasks", command=self.save_tasks)
        file_menu.add_command(label="Load Tasks", command=self.load_tasks)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
    
    

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def mark_complete(self):
        try:
            selected = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected)
            self.task_listbox.delete(selected)
            self.task_listbox.insert(tk.END, f"{task} (Completed)")
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected)
            del self.tasks[selected]
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)

    def save_tasks(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file:
            with open(file, "w") as f:
                for task in self.tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully!")

    def load_tasks(self):
        file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file:
            with open(file, "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.task_listbox.delete(0, tk.END)
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)
            messagebox.showinfo("Success", "Tasks loaded successfully!")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        # Set the background color for the main window
        self.root.configure(bg='light blue')

        self.frame = tk.Frame(self.root, bg='#f0f0f0')
        self.frame.pack(pady=10)

        self.heading = tk.Label(self.frame, text="To-Do List", font=('Helvetica', 16, 'bold'), bg='#f0f0f0')
        self.heading.pack(pady=(0, 10))

        self.task_listbox = tk.Listbox(self.frame, width=50, height=15, bg='#ffffff', fg='#000000', selectbackground='#cccccc', font=('Helvetica', 12))
        self.task_listbox.pack(side=tk.LEFT, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.button_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, bg='#4caf50', fg='#ffffff', font=('Helvetica', 10))
        self.add_button.grid(row=0, column=0, padx=8)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, bg='#2196f3', fg='#ffffff', font=('Helvetica', 10))
        self.update_button.grid(row=0, column=1, padx=8)

        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task, bg='#ffeb3b', fg='#000000', font=('Helvetica', 10))
        self.complete_button.grid(row=0, column=2, padx=8)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg='#f44336', fg='#ffffff', font=('Helvetica', 10))
        self.delete_button.grid(row=0, column=3, padx=8)

        self.load_tasks()

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.save_tasks()
            self.load_tasks()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Update Task", "Please select a task to update.")
            return

        index = selected_task_index[0]
        task = simpledialog.askstring("Update Task", "Enter the updated task:", initialvalue=self.tasks[index]["task"])
        if task:
            self.tasks[index]["task"] = task
            self.save_tasks()
            self.load_tasks()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Complete Task", "Please select a task to mark as completed.")
            return

        index = selected_task_index[0]
        self.tasks[index]["completed"] = True
        self.save_tasks()
        self.load_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")
            return

        index = selected_task_index[0]
        del self.tasks[index]
        self.save_tasks()
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

    def save_tasks(self):
        pass  # Placeholder for task persistence, e.g., saving to a file or database

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

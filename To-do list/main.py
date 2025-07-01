import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✅ To-Do List")
        self.root.geometry("450x600")
        self.root.configure(bg="#e3f2fd")
        
        self.tasks = []
        self.task_vars = []
        self.load_tasks()
        
        self.title_label = tk.Label(root, text="📌 Yapılacaklar Listesi", font=("Arial", 20, "bold"), bg="#e3f2fd", fg="#0d47a1")
        self.title_label.pack(pady=15)
        
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 14), bd=2, relief=tk.FLAT, highlightbackground="#0d47a1", highlightthickness=2)
        self.task_entry.pack(pady=10, padx=20)
        
        button_style = {"font": ("Arial", 12, "bold"), "bd": 3, "relief": tk.RIDGE, "padx": 12, "pady": 7, "borderwidth": 3, "highlightthickness": 3}
        
        self.add_button = tk.Button(root, text="➕ Ekle", command=self.add_task, bg="#43a047", fg="white", **button_style)
        self.add_button.pack(pady=5)
        
        self.frame = tk.Frame(root, bg="#e3f2fd")
        self.frame.pack(pady=10)
        
        self.task_frame = tk.Frame(self.frame, bg="#e3f2fd")
        self.task_frame.pack()
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.remove_button = tk.Button(root, text="❌ Sil", command=self.remove_task, bg="#e53935", fg="white", **button_style)
        self.remove_button.pack(pady=5)
        
        self.save_button = tk.Button(root, text="💾 Kaydet", command=self.save_tasks, bg="#ffb300", fg="white", **button_style)
        self.save_button.pack(pady=5)
        
        self.load_listbox()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.load_listbox()
    
    def remove_task(self):
        self.tasks = [task for i, task in enumerate(self.tasks) if not self.task_vars[i].get()]
        self.load_listbox()
    
    def toggle_task(self, index):
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.load_listbox()
    
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Bilgi", "Görevler kaydedildi!")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
    
    def load_listbox(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        
        self.task_vars = []
        for index, task in enumerate(self.tasks):
            var = tk.BooleanVar(value=task["completed"])
            chk = tk.Checkbutton(self.task_frame, text=task["task"], variable=var, font=("Arial", 12), bg="#e3f2fd", activebackground="#e3f2fd", command=lambda i=index: self.toggle_task(i))
            chk.pack(anchor="w", pady=5, padx=10)
            self.task_vars.append(var)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

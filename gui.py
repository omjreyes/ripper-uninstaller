import tkinter as tk
from tkinter import messagebox
from app_manager import AppManager
from datetime import datetime

class AppGUI:
    def __init__(self):
        self.manager = AppManager()
        self.root = tk.Tk()
        self.root.title("App Uninstaller Tool")
        self.root.geometry("400x600")  # Vertical window, 30% screen width (adjust as needed)
        self.setup_ui()

    def setup_ui(self):
        # App List
        self.app_listbox = tk.Listbox(self.root)
        self.app_listbox.pack(fill=tk.BOTH, expand=True)
        
        # Populate Listbox
        apps = self.manager.get_installed_apps()
        for app in sorted(apps):
            self.app_listbox.insert(tk.END, app)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X)

        uninstall_btn = tk.Button(button_frame, text="Uninstall", command=self.uninstall_app)
        uninstall_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

        repair_btn = tk.Button(button_frame, text="Repair", command=self.repair_app)
        repair_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Taskbar with live time
        self.taskbar = tk.Label(self.root, text="", anchor=tk.W)
        self.taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.taskbar.config(text=f"Time: {current_time}")
        self.root.after(1000, self.update_time)

    def uninstall_app(self):
        selected_app = self.get_selected_app()
        if selected_app:
            if messagebox.askyesno("Confirm Uninstall", f"Are you sure you want to uninstall {selected_app}?"):
                self.manager.uninstall_app(selected_app)

    def repair_app(self):
        selected_app = self.get_selected_app()
        if selected_app:
            self.manager.repair_app(selected_app)
            messagebox.showinfo("Repair", f"Repair process completed for {selected_app}.")

    def get_selected_app(self):
        try:
            return self.app_listbox.get(self.app_listbox.curselection())
        except tk.TclError:
            messagebox.showerror("Error", "No application selected.")
            return None

    def run(self):
        self.root.mainloop()
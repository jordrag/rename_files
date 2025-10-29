import os
import tkinter as tk
from tkinter import filedialog, messagebox

class RenameFilesGUI(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Renamer")
        self.root.geometry("400x200")
        
        self.folder_path = None
        self.new_name = None
        self.entry_pattern = None
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter new name pattern:").pack(pady=10)
        self.entry_pattern = tk.Entry(self.root, width=30)
        self.entry_pattern.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Select Folder", command=self.select_folder).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Start Renaming", command=self.rename_files).grid(row=0, column=1, padx=5)

    def select_folder(self):
        self.folder_path = filedialog.askdirectory(title="Select folder containing files to rename")
        if self.folder_path:
            messagebox.showinfo("Folder Selected", f"Selected folder: {self.folder_path}")

    def rename_files(self):
        self.new_name = self.entry_pattern.get()
        if not self.new_name:
            messagebox.showerror("Error", "Please enter a new name pattern")
            return
        if not self.folder_path:
            messagebox.showerror("Error", "Please select a folder first")
            return

        try:
            renamed_count = 0
            for count, filename in enumerate(os.listdir(self.folder_path), 1):
                file_ext = os.path.splitext(filename)[1]
                new_filename = f"{self.new_name}_{count}{file_ext}"
                old_file = os.path.join(self.folder_path, filename)
                new_file = os.path.join(self.folder_path, new_filename)

                try:
                    os.rename(old_file, new_file)
                    renamed_count += 1
                except OSError as e:
                    messagebox.showwarning("Warning", f"Could not rename {filename}: {e}")

            messagebox.showinfo("Success", f"Renamed {renamed_count} files in the selected folder")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RenameFilesGUI()
    app.run()
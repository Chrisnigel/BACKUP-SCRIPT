import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def backup_files(source_folder, backup_folder):
    """
    Automatically backs up files from source_folder to a timestamped folder inside backup_folder.
    """
    if not os.path.exists(source_folder):
        messagebox.showerror("Error", f"Source folder '{source_folder}' does not exist.")
        return
    
    # Create a timestamped backup folder
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_subfolder = os.path.join(backup_folder, f"backup_{timestamp}")
    os.makedirs(backup_subfolder, exist_ok=True)
    
    # Copy files from source to backup folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            shutil.copy2(file_path, backup_subfolder)
    
    messagebox.showinfo("Success", f"Backup completed successfully in '{backup_subfolder}'")

def browse_source():
    folder_selected = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, folder_selected)

def browse_backup():
    folder_selected = filedialog.askdirectory()
    backup_entry.delete(0, tk.END)
    backup_entry.insert(0, folder_selected)

def start_backup():
    source_dir = source_entry.get()
    backup_dir = backup_entry.get()
    backup_files(source_dir, backup_dir)

# GUI setup
root = tk.Tk()
root.title("Backup Script")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Source Folder:").grid(row=0, column=0, sticky="w")
source_entry = tk.Entry(frame, width=50)
source_entry.grid(row=0, column=1)
tk.Button(frame, text="Browse", command=browse_source).grid(row=0, column=2)

tk.Label(frame, text="Backup Folder:").grid(row=1, column=0, sticky="w")
backup_entry = tk.Entry(frame, width=50)
backup_entry.grid(row=1, column=1)
tk.Button(frame, text="Browse", command=browse_backup).grid(row=1, column=2)

tk.Button(frame, text="Start Backup", command=start_backup).grid(row=2, column=1, pady=10)

root.mainloop()

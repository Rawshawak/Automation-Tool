import os
import shutil
import tkinter as tk
from tkinter import filedialog

class AutomationWizard:
    def __init__(self, master):
        self.master = master
        self.master.title("File Copy Automation Wizard")

        self.source_path = ""
        self.destination_path = ""

        # Step 1: Choose source directory
        self.label1 = tk.Label(master, text="Step 1: Choose source directory")
        self.label1.pack()

        self.button1 = tk.Button(master, text="Browse", command=self.choose_source_directory)
        self.button1.pack()

        # Step 2: Choose destination directory
        self.label2 = tk.Label(master, text="Step 2: Choose destination directory")
        self.label2.pack()

        self.button2 = tk.Button(master, text="Browse", command=self.choose_destination_directory)
        self.button2.pack()

        # Step 3: Copy files
        self.label3 = tk.Label(master, text="Step 3: Copy files")
        self.label3.pack()

        self.button3 = tk.Button(master, text="Copy Files", command=self.copy_files)
        self.button3.pack()

    def choose_source_directory(self):
        self.source_path = filedialog.askdirectory()
        print("Source Directory:", self.source_path)

    def choose_destination_directory(self):
        self.destination_path = filedialog.askdirectory()
        print("Destination Directory:", self.destination_path)

    def copy_files(self):
        if not self.source_path or not self.destination_path:
            print("Please choose source and destination directories.")
            return

        try:
            files = os.listdir(self.source_path)
            for file in files:
                source_file_path = os.path.join(self.source_path, file)
                destination_file_path = os.path.join(self.destination_path, file)
                shutil.copy(source_file_path, destination_file_path)

            print("Files copied successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationWizard(root)
    root.mainloop()

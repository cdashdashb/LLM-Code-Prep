import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import pyperclip


class CodeFormatter:
    def __init__(self, master):
        self.master = master
        self.master.title("LLM Code Prep")
        self.master.geometry("500x400")

        self.processed_files = set()

        self.create_widgets()

    def create_widgets(self):
        # Frame for buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10, fill=tk.X)

        # Select and Clear buttons side by side
        self.select_button = tk.Button(
            self.button_frame, text="Select Files", command=self.select_files, width=20
        )
        self.select_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear Selected Files",
            command=self.clear_files,
            width=20,
        )
        self.clear_button.pack(side=tk.RIGHT, padx=5)

        # Listbox for selected files
        self.file_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE)
        self.file_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Process buttons
        self.process_button = tk.Button(
            self.master,
            text="Process Files and Save",
            command=self.process_files,
            width=25,
        )
        self.process_button.pack(pady=5)

        self.copy_button = tk.Button(
            self.master,
            text="Process Files and Copy to Clipboard",
            command=self.copy_to_clipboard,
            width=35,
        )
        self.copy_button.pack(pady=5)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(
            filetypes=[
                ("C# files", "*.cs"),
                ("Python files", "*.py"),
                ("Text files", "*.txt"),
                ("All files", "*.*"),
            ]
        )
        for file_path in file_paths:
            if file_path not in self.processed_files:
                self.file_listbox.insert(tk.END, file_path)
                self.processed_files.add(file_path)

    def clear_files(self):
        self.file_listbox.delete(0, tk.END)
        self.processed_files.clear()

    def format_files(self):
        if not self.processed_files:
            messagebox.showwarning("Warning", "No files selected!")
            return None

        output = []
        for file_path in self.processed_files:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                file_name = os.path.basename(file_path)
                formatted_content = f"`{file_name}`\n```\n{content}\n```\n\n"
                output.append(formatted_content)

        return "\n".join(output)

    def process_files(self):
        formatted_text = self.format_files()
        if formatted_text:
            output_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text files", "*.txt")]
            )
            if output_path:
                with open(output_path, "w", encoding="utf-8") as output_file:
                    output_file.write(formatted_text)

                # Open the output file in the default text editor
                subprocess.run(["start", "", output_path], shell=True)

    def copy_to_clipboard(self):
        formatted_text = self.format_files()
        if formatted_text:
            pyperclip.copy(formatted_text)
            messagebox.showinfo("Success", "Formatted text copied to clipboard!")


def main():
    root = tk.Tk()
    app = CodeFormatter(root)
    root.mainloop()


if __name__ == "__main__":
    main()

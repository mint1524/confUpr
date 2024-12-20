import csv
import os
import tarfile
import datetime
import tkinter as tk
from tkinter import scrolledtext, messagebox

def read_config(config_path):
    config = {}
    with open(config_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            config[row[0]] = row[1]
    return config

def log_action(log_file, user, command):
    with open(log_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([user, command, str(datetime.datetime.now())])

def ls_command(current_directory, tar_path):
    with tarfile.open(tar_path, 'r') as tar:
        files = []
        for member in tar.getmembers():
            if member.name.startswith("." + current_directory):
                foo = member.name.replace("." + current_directory, "")
                if '/' not in foo.strip('./').strip('/'):
                    files.append(foo.strip('./').strip('/'))
        if files[0] == '':
            files.pop(0)
    return files

def cd_command(current_directory, new_dir, tar_path):
    if new_dir == "..":
        if current_directory == '/':
            new_path = '/'
        else:
            new_path = os.path.dirname(current_directory.strip('/'))
            if not new_path: 
                new_path = '/'
    else:
        new_path = os.path.join(current_directory, new_dir).strip('/')
    with tarfile.open(tar_path, 'r') as tar:
        directories = [member.name.strip('/') for member in tar.getmembers() if member.isdir()]
        if new_path == '/':
            return '/'  
        elif any(d == new_path or d == f'./{new_path}' for d in directories):
            return '/' + new_path  
        else:
            raise FileNotFoundError(f"Directory {new_dir} not found")

def head_command(file_path, tar_path, lines=10):
    with tarfile.open(tar_path, 'r') as tar:
        try:
            if not file_path.startswith('./'):
                file_path = './' + file_path  
            file = tar.extractfile(file_path)
            if file:
                return ''.join(file.readline().decode() for _ in range(lines))
        except KeyError:
            raise FileNotFoundError(f"File {file_path} not found")

class ShellEmulator(tk.Tk):
    def __init__(self, config):
        super().__init__()
        self.title("Shell Emulator")
        self.geometry("800x600")
        
        self.user = config['user']
        self.tar_path = config['tar_path']
        self.log_file = config['log_path']
        self.current_directory = '/'
        
        self.prompt = f"{self.user}@shell:{self.current_directory}$ "
        self.input_field = tk.Entry(self, font=("Consolas", 12))
        self.input_field.pack(fill=tk.X, padx=10, pady=10)
        self.input_field.bind('<Return>', self.process_command)

        self.output_area = scrolledtext.ScrolledText(self, font=("Consolas", 12), wrap=tk.WORD)
        self.output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.write_output("Welcome to the Shell Emulator!\nType 'exit' to quit.\n")

    def process_command(self, event=None):
        command = self.input_field.get().strip()
        self.write_output(f"{self.prompt}{command}\n")
        self.input_field.delete(0, tk.END)

        log_action(self.log_file, self.user, command)

        # Обработка команды
        if command.startswith("ls"):
            self.ls()
        elif command.startswith("cd"):
            self.cd(command.split()[1] if len(command.split()) > 1 else "/")
        elif command.startswith("clear"):
            self.clear()
        elif command.startswith("head"):
            self.head(command.split()[1] if len(command.split()) > 1 else "")
        elif command == "exit":
            self.quit_shell()
        else:
            self.write_output(f"Command '{command}' not found.\n")

    def ls(self):
        try:
            files = ls_command(self.current_directory, self.tar_path)
            self.write_output("\n".join(files) + "\n")
        except Exception as e:
            self.write_output(f"Error: {str(e)}\n")

    def cd(self, directory):
        try:
            self.current_directory = cd_command(self.current_directory, directory, self.tar_path)
            self.prompt = f"{self.user}@shell:{self.current_directory}$ "
        except FileNotFoundError as e:
            self.write_output(f"Error: {str(e)}\n")

    def clear(self):
        self.output_area.delete(1.0, tk.END)

    def head(self, file_path):
        try:
            content = head_command(file_path, self.tar_path)
            self.write_output(content)
        except FileNotFoundError as e:
            self.write_output(f"Error: {str(e)}\n")

    def quit_shell(self):
        self.write_output("Exiting shell...\n")
        self.after(1000, self.quit)

    def write_output(self, text):
        self.output_area.insert(tk.END, text)
        self.output_area.yview(tk.END)

# Запуск эмулятора
if __name__ == "__main__":
    config = read_config('config.csv')
    app = ShellEmulator(config)
    app.mainloop()

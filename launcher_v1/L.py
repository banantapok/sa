import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import configparser

config = configparser.ConfigParser()
config.read("launcher_config.ini")

def save_config():
    config["Settings"]["samp_folder"] = samp_folder_path.get()
    config["Settings"]["nickname"] = nickname_entry.get()

    with open("launcher_config.ini", "w") as config_file:
        config.write(config_file)

def launch_samp():
    samp_path = samp_folder_path.get()
    selected_server = server_combo.get()
    server_info = server_options[selected_server]
    server_ip = server_info["ip"]
    server_port = server_info["port"]

    nickname = nickname_entry.get()

    os.chdir(samp_path)
    os.system(f'samp.exe {server_ip}:{server_port} -n{nickname}')

def select_samp_folder():
    folder_path = filedialog.askdirectory()
    samp_folder_path.set(folder_path)

def exit_launcher():
    save_config()
    root.destroy()

root = tk.Tk()
root.title("SampRax Launcher")
root.geometry("370x380")
root.configure(bg="purple")
root.resizable(width=False, height=False)  # Запрет изменения размера окна

background_image = Image.open("samp_logo.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

samp_folder_path = tk.StringVar()
samp_folder_path.set(config["Settings"].get("samp_folder", "Введите путь к папке с SAMP"))

nickname_entry = tk.StringVar()
nickname_entry.set(config["Settings"].get("nickname", "Ваш никнейм"))

samp_label = tk.Label(root, text="SampRax", font=("Helvetica", 18, "bold"), bg="purple")
samp_label.pack(pady=10)

label = tk.Label(root, text="Выберите папку с SAMP:", bg="purple")
label.pack(pady=10)

entry = tk.Entry(root, textvariable=samp_folder_path, bg="purple")
entry.pack(pady=5)

browse_button = tk.Button(root, text="Обзор...", command=select_samp_folder, bg="purple")
browse_button.pack()

server_label = tk.Label(root, text="Выберите сервер:", bg="purple")
server_label.pack(pady=5)

server_options = {
    "SampRax Server 1": {"ip": "185.189.15.22", "port": "2394"},
    "Недоступен Server 2": {"ip": "185.189.15.22", "port": "2394"}  # Пример другого сервера
}  # Словарь серверов
server_combo = ttk.Combobox(root, values=list(server_options.keys()), background="purple")
server_combo.pack()

nickname_label = tk.Label(root, text="Введите ваш никнейм:", bg="purple")
nickname_label.pack(pady=5)

nickname_input = tk.Entry(root, textvariable=nickname_entry, bg="purple")
nickname_input.pack()

launch_button = tk.Button(root, text="Запустить SAMP", command=launch_samp, bg="purple", height=2, font=("Helvetica", 12))
launch_button.pack(pady=20)

exit_button = tk.Button(root, text="Закрыть", command=exit_launcher, bg="purple")
exit_button.pack(pady=5)

root.mainloop()

import subprocess
import tkinter as tk
from tkinter import ttk
import pickle
from pathlib import Path
import sqlite3

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Роман\Desktop\PraktikaKafe\build\SmenaPostavit\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_first_form():
    window.destroy()
    subprocess.Popen(["Python","First.py"])

def open_back_form():
    window.destroy()
    subprocess.Popen(["Python","Smena.py"])

def save_values():
    with open("values.pkl", "wb") as f:
        pickle.dump((entry_1.get(), combo_1.get(), combo_2.get()), f)

def load_values():
    try:
        with open("values.pkl", "rb") as f:
            date, cook, waiter = pickle.load(f)
            entry_1.delete(0, tk.END)
            entry_1.insert(0, date)
            combo_1.set(cook)
            combo_2.set(waiter)
    except FileNotFoundError:
        pass

window = tk.Tk()
window.geometry("372x282")
window.configure(bg="#FFFFFF")

canvas = tk.Canvas(
    window,
    bg="#FFFFFF",
    height=282,
    width=372,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = tk.PhotoImage(
    file=relative_to_assets("image_1.png")
)
image_1 = canvas.create_image(
    265.0,
    141.0,
    image=image_image_1
)

canvas.create_text(
    52.0,
    42.0,
    anchor="nw",
    text="Смены",
    fill="#996633",
    font=("ComingSoon Regular", 15 * -1)
)

canvas.create_text(
    11.0,
    68.0,
    anchor="nw",
    text="Дата:",
    fill="#996633",
    font=("ComingSoon Regular", 15 * -1)
)

canvas.create_text(
    10.0,
    102.0,
    anchor="nw",
    text="Повар:",
    fill="#996633",
    font=("ComingSoon Regular", 15 * -1)
)

canvas.create_text(
    11.0,
    136.0,
    anchor="nw",
    text="Офик:",
    fill="#996633",
    font=("ComingSoon Regular", 15 * -1)
)

entry_image_1 = tk.PhotoImage(
    file=relative_to_assets("entry_1.png")
)
entry_bg_1 = canvas.create_image(
    100.5,
    79.0,
    image=entry_image_1
)
entry_1 = tk.Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=67.0,
    y=68.0,
    width=67.0,
    height=20.0
)

# Загрузка поваров и официантов из базы данных
def load_cooks_from_database():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM cooks')
    cooks = cursor.fetchall()
    conn.close()
    return [cook[0] for cook in cooks]

def load_waiters_from_database():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM waiters')
    waiters = cursor.fetchall()
    conn.close()
    return [waiter[0] for waiter in waiters]

combo_1 = ttk.Combobox(window)
combo_1.place(x=67.0, y=101.0, width=67.0, height=20.0)
combo_1['values'] = load_cooks_from_database()

combo_2 = ttk.Combobox(window)
combo_2.place(x=67.0, y=134.0, width=67.0, height=20.0)
combo_2['values'] = load_waiters_from_database()

# Загрузка значений по умолчанию
load_values()

button_image_3 = tk.PhotoImage(
    file=relative_to_assets("button_3.png")
)
button_3 = tk.Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=save_values and open_back_form,
    relief="flat"
)
button_3.place(
    x=37.0,
    y=171.0,
    width=100.0,
    height=25.0
)

button_image_1 = tk.PhotoImage(
    file=relative_to_assets("button_1.png")
)
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_first_form,
    relief="flat"
)
button_1.place(
    x=5.0,
    y=0.0,
    width=87.0,
    height=31.0
)

button_image_2 = tk.PhotoImage(
    file=relative_to_assets("button_2.png")
)
button_2 = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_back_form,
    relief="flat"
)
button_2.place(
    x=5.0,
    y=248.0,
    width=100.0,
    height=25.0
)

window.resizable(False, False)
window.mainloop()



from pathlib import Path
import subprocess
import sqlite3
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Роман\Desktop\PraktikaKafe\build\AdminDdobavitOfPov\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add_user_to_db(username: str, password: str):
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO waiters (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def open_first_form():
    window.destroy()
    subprocess.Popen(["Python","First.py"])

def open_back_form():
    window.destroy()
    subprocess.Popen(["Python","AdminDobavit.py"])

def handle_login():
    username = entry_1.get()
    password = entry_2.get()
    add_user_to_db(username, password)
    open_first_form()

window = Tk()
window.geometry("372x282")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 282,
    width = 372,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    265.0,
    141.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
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

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    91.5,
    89.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=49.0,
    y=80.0,
    width=85.0,
    height=17.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    91.5,
    134.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=49.0,
    y=125.0,
    width=85.0,
    height=17.0
)

canvas.create_text(
    73.0,
    57.0,
    anchor="nw",
    text="Login",
    fill="#996633",
    font=("ComingSoon Regular", 15 * -1)
)

canvas.create_text(
    59.0,
    106.0,
    anchor="nw",
    text="Password",
    fill="#996633",
    font=("ComingSoon Regular", 15 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=handle_login,  # Обработчик кнопки для добавления логина и пароля в базу данных
    relief="flat"
)
button_3.place(
    x=42.0,
    y=161.0,
    width=100.0,
    height=25.0
)

window.resizable(False, False)
window.mainloop()

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, ttk
import sqlite3
from datetime import datetime
from pathlib import Path
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Роман\Desktop\PraktikaKafe\build\OfikZakaz\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_back_form():
    window.destroy()
    subprocess.Popen(["Python","Ofik1.py"])

def open_first_form():
    window.destroy()
    subprocess.Popen(["Python","First.py"])

def save_to_database(item, hour, minute, status):
    time = f"{hour:02d}:{minute:02d}:00"
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (item, time, status) VALUES (?, ?, ?)', (item, time, status))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Заказ сохранен в базе данных.")

def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

window = Tk()

window.geometry("372x282")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=282,
    width=372,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

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
    command=open_back_form,
    relief="flat"
)
button_1.place(
    x=9.0,
    y=248.0,
    width=100.0,
    height=25.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_to_database(entry_1.get(), int(combo_hour.get()), int(combo_minute.get()), "Принят"),
    relief="flat"
)
button_2.place(
    x=33.0,
    y=167.0,
    width=100.0,
    height=25.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_first_form,
    relief="flat"
)
button_3.place(
    x=5.0,
    y=0.0,
    width=54.0,
    height=31.0
)

canvas.create_text(
    5.0,
    39.0,
    anchor="nw",
    text="Наименование заказа",
    fill="#996633",
    font=("ComingSoon Regular", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    81.0,
    76.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=12.0,
    y=61.0,
    width=138.0,
    height=28.0
)

canvas.create_text(
    33.0,
    99.0,
    anchor="nw",
    text="Время заказа",
    fill="#996633",
    font=("ComingSoon Regular", 14 * -1)
)

# Создаем Combobox для выбора часов
combo_hour = ttk.Combobox(window)
combo_hour.place(x=12.0, y=121.0, width=70.0, height=28.0)
combo_hour['values'] = [str(i).zfill(2) for i in range(1, 25)]  # Часы от 1 до 24

# Создаем Combobox для выбора минут
combo_minute = ttk.Combobox(window)
combo_minute.place(x=80.0, y=121.0, width=70.0, height=28.0)
combo_minute['values'] = [str(i).zfill(2) for i in range(0, 60)]  # Минуты от 0 до 59

window.resizable(False, False)
window.mainloop()


from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
import sqlite3
from pathlib import Path
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Роман\Desktop\PraktikaKafe\build\UvolitOfPov\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_first_form():
    window.destroy()
    subprocess.Popen(["Python","First.py"])

def open_back_form():
    window.destroy()
    subprocess.Popen(["Python","Uvolit.py"])

def remove_waiter(waiter):
    confirmation = messagebox.askyesno("Уволить", f"Вы точно хотите уволить {waiter}?")
    if confirmation:
        conn = sqlite3.connect('cafe.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM waiters WHERE username = ?', (waiter,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", f"{waiter} был уволен.")

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
    text="Уволить",
    fill="#996633",
    font=("ComingSoon Regular", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")
)
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
    file=relative_to_assets("button_2.png")
)
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

# Загрузка официантов из базы данных
def load_waiters_from_database():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM waiters')
    waiters = cursor.fetchall()
    conn.close()
    return [waiter[0] for waiter in waiters]

waiters = load_waiters_from_database()
for i, waiter in enumerate(waiters):
    btn = Button(window, text=f"Уволить {waiter}", command=lambda w=waiter: remove_waiter(w))
    btn.place(x=10, y=70 + 30 * i, width=150, height=25)

window.resizable(False, False)
window.mainloop()

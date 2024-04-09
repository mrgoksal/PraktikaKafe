from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import sqlite3
from pathlib import Path
import subprocess
from tkinter import ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Роман\Desktop\PraktikaKafe\build\PovarZakStat\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_first_form():
    window.destroy()
    subprocess.Popen(["Python", "First.py"])

def save_to_database(item, status):
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()

    # Проверяем, существует ли заказ с выбранным элементом
    cursor.execute('SELECT id FROM orders WHERE item = ?', (item,))
    existing_order = cursor.fetchone()

    if existing_order:
        # Если заказ существует, обновляем его статус
        cursor.execute('UPDATE orders SET status = ? WHERE item = ?', (status, item))
    else:
        # Если заказ не существует, создаем новый заказ
        cursor.execute('INSERT INTO orders (item, status) VALUES (?, ?)', (item, status))

    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Заказ сохранен в базе данных.")

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
    command=open_first_form,
    relief="flat"
)
button_1.place(
    x=5.0,
    y=0.0,
    width=62.0,
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

# Создаем Combobox для выбора блюд из базы данных
def load_dishes_from_database():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT item FROM orders')
    dishes = cursor.fetchall()
    conn.close()
    return [dish[0] for dish in dishes]

combo_item = ttk.Combobox(window)
combo_item.place(x=17.0, y=65.0, width=138.0, height=28.0)
combo_item['values'] = load_dishes_from_database()

canvas.create_text(
    32.0,
    99.0,
    anchor="nw",
    text="Статус заказа",
    fill="#996633",
    font=("ComingSoon Regular", 14 * -1)
)

# Создаем Combobox для выбора статуса заказа
combo_status = ttk.Combobox(window)
combo_status.place(x=17.0, y=136.0, width=138.0, height=28.0)
combo_status['values'] = ("Принят", "Готовится", "Готов")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_to_database(combo_item.get(), combo_status.get()),
    relief="flat"
)
button_2.place(
    x=33.0,
    y=167.0,
    width=100.0,
    height=25.0
)
window.resizable(False, False)
window.mainloop()

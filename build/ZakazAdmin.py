from tkinter import Tk, Canvas, Button, PhotoImage, messagebox, Scrollbar
import sqlite3
from pathlib import Path
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Роман\Desktop\PraktikaKafe\build\ZakazAdmin\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_first_form():
    window.destroy()
    subprocess.Popen(["Python", "First.py"])


def open_back_form():
    window.destroy()
    subprocess.Popen(["Python", "Adminka.py"])


def load_orders_from_database():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, item FROM orders')
    orders = cursor.fetchall()
    conn.close()
    return orders


def show_order_info(order_id):
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders WHERE id=?', (order_id,))
    order_info = cursor.fetchone()
    conn.close()

    order_info_window = Tk()
    order_info_window.title("Информация о заказе")

    order_info_text = f"ID: {order_info[0]}\nTime: {order_info[1]}\nItem: {order_info[2]}\nStatus: {order_info[3]}"
    order_info_label = Canvas(order_info_window, bg="#FFFFFF", width=300, height=100)
    order_info_label.pack()

    order_info_label.create_text(150, 50, text=order_info_text, fill="#000000", font=("Arial", 12))

    delete_button = Button(order_info_window, text="Удалить заказ", command=lambda: delete_order(order_id, order_info_window))
    delete_button.pack()

    order_info_window.mainloop()


def delete_order(order_id, window):
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM orders WHERE id=?', (order_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Заказ успешно удален.")
    window.destroy()


def create_order_buttons():
    orders = load_orders_from_database()
    for order in orders:
        order_button = Button(order_canvas, text=order[1], command=lambda id=order[0]: show_order_info(id))
        order_canvas.create_window(10, len(order_buttons) * 30 + 60, window=order_button, anchor='nw')
        order_buttons.append(order_button)


def on_mouse_wheel(event):
    order_canvas.yview_scroll(int(-1*(event.delta/120)), "units")


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

order_canvas = Canvas(window, bg="#FFFFFF", height=170, width=135)
order_canvas.place(x=10, y=60)

order_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

scrollbar = Scrollbar(window, orient="vertical", command=order_canvas.yview)
scrollbar.place(x=135, y=60, height=170)

order_canvas.config(yscrollcommand=scrollbar.set)

order_buttons = []

create_order_buttons()

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

window.mainloop()



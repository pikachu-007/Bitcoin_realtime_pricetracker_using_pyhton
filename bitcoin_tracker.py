import requests
import tkinter as tk
from datetime import datetime

def trackbit():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = request.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")
    labelPrice.config(text = str(price) + "$")
    labelTime.config(text = "at" + time)
canvas=tk.Tk()
canvas.geometry("500x500")
canvas.title("Bitcoin")
f1 = ("poppins",24,"bold")
f2 = ("poppins",22,"bold")
f3 = ("poppins",18,"normal")

label = tk.Label(canvas,text = "bitcoin price", font = f1)
label.pack( pady = 20)

labelPrice = tk.Label(canvas,font = f2)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas,font = f3)
labelPrice.pack(pady = 20)

canvas.mainloop()
    
import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io

API_KEY = 'fc7fda8066ad1c9db10410d2a950f580'


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_icon = data['weather'][0]['icon']
        return temperature, weather_icon
    else:
        return None, None


def show_weather():
    city = city_entry.get()
    temperature, weather_icon = get_weather(city)
    if temperature is not None:
        temperature_label.config(text=f"Температура: {temperature}°C")
        update_weather_icon(weather_icon)
    else:
        temperature_label.config(text="Город не найден!")


def update_weather_icon(icon_code):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    image_data = io.BytesIO(response.content)
    image = Image.open(image_data)
    image = image.resize((100, 100), Image.ANTIALIAS)
    weather_icon_image = ImageTk.PhotoImage(image)

    icon_label.config(image=weather_icon_image)
    icon_label.image = weather_icon_image



root = tk.Tk()
root.title("Погодное приложение")
root.geometry("300x200")


city_label = ttk.Label(root, text="Введите город:")
city_label.pack(pady=10)

city_entry = ttk.Entry(root)
city_entry.pack(pady=10)

get_weather_button = ttk.Button(root, text="Получить погоду", command=show_weather)
get_weather_button.pack(pady=10)

temperature_label = ttk.Label(root, text="")
temperature_label.pack(pady=10)

icon_label = ttk.Label(root)
icon_label.pack(pady=10)

root.mainloop()


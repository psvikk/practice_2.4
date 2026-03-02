import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io

def get_random_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        cat_data = response.json()
        cat_image_url = cat_data[0]['url']
        update_image(cat_image_url)

def get_random_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        dog_data = response.json()
        dog_image_url = dog_data['message']
        update_image(dog_image_url)

def update_image(image_url):
    response = requests.get(image_url)
    image_data = io.BytesIO(response.content)
    image = Image.open(image_data)
    image = image.resize((300, 300), Image.ANTIALIAS)  # Измените размер изображения по желанию
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo  # Сохраняем ссылку на изображение

root = tk.Tk()
root.title("Коты и Собаки")
root.geometry("400x400")

cat_button = ttk.Button(root, text="Получить кота", command=get_random_cat)
cat_button.pack(pady=10)

dog_button = ttk.Button(root, text="Получить собаку", command=get_random_dog)
dog_button.pack(pady=10)

image_label = ttk.Label(root)
image_label.pack(pady=10)

root.mainloop()

import tkinter as tk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600


def test_function(entry):
    print("This is the entry:", entry)


def format_response(weather):
    try:
        name = weather['city']['name']
        desc = weather['list'][0]['main']['temp']
        temp = weather['list'][0]['weather'][0]['description']

        final_str =  'City: %s \nConditions: %s\nTemperature (F): %s' % (name,desc,temp)

    except:
        final_str = "There was a problem retrieving that info"
    return final_str


def get_weather(city):
    weather_key = 'a5955b52590a4018bf8df16a7f55e26b'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather_json = response.json()

    label['text'] = format_response(weather_json)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)
root.mainloop()

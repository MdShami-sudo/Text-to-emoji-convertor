import tkinter as tk
from tkinter import ttk
import random

emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "sun": "☀️",
    "star": "⭐",
    "cat": "🐱",
    "dog": "🐶",
    "pizza": "🍕",
    "coffee": "☕",
    "heart": "❤️",
    "fire": "🔥",
    "flower": "🌸",
}

def text_to_emoji(text):
    words = text.split()
    new_words = []
    for word in words:
        if word in emoji_dict and random.random() < 0.5:
            new_words.append(emoji_dict[word])
        else:
            new_words.append(word)
    return " ".join(new_words)

def convert_text():
    input_text = input_text_var.get()
    output_text = text_to_emoji(input_text)
    output_label_var.set(output_text)

def draw_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    limit = height

    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))

        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

root = tk.Tk()
root.title("Random Text to Emoji Converter")
root.geometry("400x300")

gradient_canvas = tk.Canvas(root, width=400, height=300)
gradient_canvas.pack(fill="both", expand=True)

root.update_idletasks()  
draw_gradient(gradient_canvas, "#ffcccc", "#cc99ff")

frame = ttk.Frame(gradient_canvas)
frame.place(relx=0.5, rely=0.5, anchor="center")

input_label = ttk.Label(frame, text="Enter your text:")
input_label.pack(pady=5)

input_text_var = tk.StringVar()
input_text_entry = ttk.Entry(frame, textvariable=input_text_var, width=50)
input_text_entry.pack(pady=5)

convert_button = ttk.Button(frame, text="Convert to Emoji", command=convert_text)
convert_button.pack(pady=10)

output_label_var = tk.StringVar()
output_label = ttk.Label(frame, textvariable=output_label_var, wraplength=350)
output_label.pack(pady=5)

root.mainloop()

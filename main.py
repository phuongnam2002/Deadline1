import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
#from model import*

app = tk.Tk()
app.geometry("532x632")
app.title("CLB Lập Trình PTIT")
ctk.set_appearance_mode("blue")
prompt = ctk.CTkEntry(height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)
screen = ctk.CTkLabel(height=512, width=512)
screen.place(x=10, y=110)


# def gene():
#     with autocast(device):
#         image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
#
#     image.save('generate.png')
#     img = ImageTk.PhotoImage(image)
#     screen.configure(image=img)


trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="blue")
                        #command=gene)
trigger.configure(text="Enter")
trigger.place(x=206, y=60)

app.mainloop()

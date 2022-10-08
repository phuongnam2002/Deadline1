import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
model = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(model, torch_dtype=torch.float16,
                                               revision="fp16",
                                               use_auth_token="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")
pipe = pipe.to(device)

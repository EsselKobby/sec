# Import of required libraries
import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
from PIL import Image, ImageTk
 

 # Main Window Initialization
root = tk.Tk()
root.title("Universal Password Cracker")
root.geometry("800*700")

# Path to Bundled Resources Functions (Logo Image)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Window Icon Set-Up
logo = Image.open(resource_path("logo.png"))
logo = logo.resize((64, 64), Image.LANCZOS)
logo = ImageTk.photoImage(logo)
root.iconphoto(False, logo)


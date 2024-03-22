import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import cv2
from PIL import Image, ImageTk
import numpy as np
from matplotlib import pyplot as plt

def analyze_image_gui(image_path, target_size=(350, 250), threshold_value=127):
    # Load image
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Resize image
    resized_image = cv2.resize(original_image, target_size)

    # Apply binary thresholding
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Convert CV2 images to PIL format
    original_image_pil = Image.fromarray(original_image)
    resized_image_pil = Image.fromarray(resized_image)
    binary_image_pil = Image.fromarray(binary_image)

    # Display images using labels
    original_photo = ImageTk.PhotoImage(original_image_pil)
    resized_photo = ImageTk.PhotoImage(resized_image_pil)
    binary_photo = ImageTk.PhotoImage(binary_image_pil)

    original_label.configure(image=original_photo)
    original_label.image = original_photo

    resized_label.configure(image=resized_photo)
    resized_label.image = resized_photo

    binary_label.configure(image=binary_photo)
    binary_label.image = binary_photo

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Default values
        target_size = (350, 250)
        threshold_value = 127
        
        # Prompt for target size and threshold
        target_size_str = simpledialog.askstring("Input", "Enter target size as WxH (e.g., 350x250):", parent=root)
        if target_size_str:
            width, height = map(int, target_size_str.split('x'))
            target_size = (width, height)
        
        threshold_value_str = simpledialog.askstring("Input", "Enter threshold value (0-255):", parent=root)
        if threshold_value_str:
            threshold_value = int(threshold_value_str)
        
        analyze_image_gui(file_path, target_size, threshold_value)

root = tk.Tk()
root.title("Image Analysis Tool")

# Frame for the buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(fill=tk.X)

# Frame for the images
frame_images = tk.Frame(root)
frame_images.pack()

btn_select_image = tk.Button(frame_buttons, text="Select Image", command=select_image)
btn_select_image.pack(side=tk.LEFT, padx=10, pady=10)

original_label = tk.Label(frame_images)
original_label.grid(row=0, column=0, padx=10, pady=10)

resized_label = tk.Label(frame_images)
resized_label.grid(row=0, column=1, padx=10, pady=10)

binary_label = tk.Label(frame_images)
binary_label.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()

import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from imageai.Detection import ObjectDetection
from tkinter import *
import os
from PIL import ImageTk, Image

exec_path = os.getcwd()

def open_file():
    filepath = askopenfilename(
        filetypes=[("JPEG", "*.jpg"), ("All Files", "*.*")]
    )
    newdetector = ObjectDetection()
    newdetector.setModelTypeAsRetinaNet()
    newdetector.setModelPath(os.path.join(exec_path, "resnet50_coco_best_v2.1.0.h5"))
    newdetector.loadModel()
    newdetections = newdetector.detectObjectsFromImage(input_image=os.path.join(exec_path, filepath),
                                                       output_image_path=os.path.join(exec_path, "imagenew.jpg"))
    window.imagechange2 = ImageTk.PhotoImage(Image.open("imagenew.jpg"))
    window.verdict.configure(image=window.imagechange2)
    
window = tk.Tk()
labelFont = tkFont.Font(family="Lucida Grande", size=16)
window.verdict = Label(window, text="Выберите изображение",font=labelFont)
window.title("Image Detection")
window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=1300, weight=1)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
window.verdict.grid(row=0,column=1,stick="ns",padx=1,pady=1)


window.mainloop()

import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from imageai.Detection import ObjectDetection, VideoObjectDetection
from tkinter import *
import os
import time
from PIL import ImageTk, Image

exec_path = os.getcwd()

def open_image():
    window.verdict.config(text="Фото готовится")
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

def open_video():
    window.verdict.config(text="Видео в папке проекта")
    filepath = askopenfilename(
        filetypes=[("all video format", "*.mp4"), ("All Files", "*.*")]
    )
    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(exec_path, "yolo.h5"))
    detector.loadModel()

    video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(exec_path, filepath),
                                                 output_file_path=os.path.join(exec_path, "traffic_detected"),
                                                 frames_per_second=20,
                                                 log_progress=True)



window = tk.Tk()
labelFont = tkFont.Font(family="Lucida Grande", size=16)
window.verdict = Label(window, text="Выберите файл",font=labelFont)
window.title("Image Detection")
window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=1300, weight=1)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

btn_open_image = tk.Button(fr_buttons, text="Фото", command=open_image)
btn_open_video = tk.Button(fr_buttons, text="Видео", command=open_video)

btn_open_image.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open_video.grid(row=20, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
window.verdict.grid(row=0,column=1,stick="ns",padx=1,pady=1)

window.mainloop()

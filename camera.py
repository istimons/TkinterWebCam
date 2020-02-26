"""

camera.py

This programs allows us to show camera in tkinter.

@Author _istimons
@Version 1.0 11/2019


"""


import tkinter
from tkinter import *
from tkinter import ttk

import PIL.Image
import PIL.ImageTk
import cv2
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure

Main_label_font = "-family {Perpetua Titling MT} -size 40 -weight normal -slant roman -underline 0 -overstrike 0"
Constant_val_font = "-family {Perpetua Titling MT} -size 25 -weight normal -slant roman -underline 0 -overstrike 0"


class App:

    """ This shows a variable type, used to show how the type of variable should be.
        (ie statically typed control to the dynamically typed Python)
            photo: PhotoImage
    """

    def __init__(self):

        """ open computer web camera """

        self.vid = cv2.VideoCapture(0)

        self.root = Tk()
        self.root.wm_title("Tkinter Camera")

        ''' Create a main window top color Label'''

        color_label = ttk.Label(self.root, background='blue', font=Main_label_font)
        color_label.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=4)

        ''' Canvas to encapsulate camera frame; 
            Create a canvas that can fit the above video source size         '''

        self.canvas = tkinter.Canvas(self.root)
        self.canvas.place(relx=0.02, rely=0.21, relheight=0.45, relwidth=0.6)

        ''' Label for constant changing values '''

        self.lbl_const_val = ttk.Label(self.root, text="Constant Values", font=Constant_val_font)
        self.lbl_const_val.place(relx=0.67, rely=0.15, relheight=0.05, relwidth=0.22)

        ''' Camera Label to hold the camera Label name '''

        self.lbl_cont_val = ttk.Label(self.root, text="Camera", font=Constant_val_font)
        self.lbl_cont_val.place(relx=0.15, rely=0.15, relheight=0.05, relwidth=0.19)

        ''' mainloop Exit Button'''

        self.exit_btn = ttk.Button(self.root, text="Exit", command=self.__del__)
        self.exit_btn.place(relx=0.75, rely=0.06, relheight=0.035, relwidth=0.13)

        ''' After this is called once, the update method will automatically be called every delay milliseconds '''

        self.delay = 15
        self.update()

        ''' Graph Figure and data
            This graph will be improved to constantly show constant changing values
        '''

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.t = np.arange(0, 3, .01)
        self.fig.add_subplot(111).plot(self.t, 2 * np.sin(2 * np.pi * self.t))

        ''' plotting Canvas. A tk.DrawingArea.'''

        self.graghPlot = FigureCanvasTkAgg(self.fig, master=self.root)
        self.graghPlot.draw()
        self.graghPlot.get_tk_widget().place(relx=0.02, rely=0.61, relheight=0.37, relwidth=0.5)

    def update(self):
        """ Get a frame from the video source (Real time Video Frames Update By Web The Camera)"""
        ret, frame = self.get_frame

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.root.after(self.delay, self.update)

    @property
    def get_frame(self):

        """ The property method takes the get as an arg and returns required objects
            of the get_frame in this class
            Real Time Values Update in a tkinter Label (How To)
        """

        if self.vid.isOpened():
            ret, frame = self.vid.read()

            values = "%s\n" % frame[0:-1]

            const_lbl = Label(self.root, text=values, bg='black', fg='white')
            const_lbl.place(relx=0.53, rely=0.21, relheight=0.34, relwidth=0.45)

            if ret:
                ''' Return a boolean success flag and the current frame converted to BGR '''
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
            else:
                return ret, None
        else:
            return None

    ''' Release the video source when the object is destroyed '''
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            self.root.destroy()


''' Start Application '''
app = App()

''' Get screen width and height to have a large screen'''

ws = app.root.winfo_screenwidth()  # width of the screen
hs = app.root.winfo_screenheight()  # height of the screen

app.root.geometry('%dx%d' % (ws, hs))
app.root.mainloop()

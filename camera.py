"""
_istimons

tkinter GUI gave it a shot; webCam in tkinter

"""

import tkinter
from tkinter import *
from tkinter import ttk

import PIL.Image
import PIL.ImageTk
import cv2
import numpy as np
from PIL.ImageTk import PhotoImage
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure

Main_label_font = "-family {Perpetua Titling MT} -size 40 -weight normal -slant roman -underline 0 -overstrike 0"
Constant_val_font = "-family {Perpetua Titling MT} -size 25 -weight normal -slant roman -underline 0 -overstrike 0"


class App(object):
    """ This shows a variable type, used to show how the type of variable should be.
        (ie statically typed control to the dynamically typed Python)
            photo: PhotoImage
    """

    photo: PhotoImage

    def __init__(self):

        self.root = Tk()
        self.root.wm_title("Tkinter Camera")

        """ Tkinter Labels """
        self.canvas = tkinter.Canvas(self.root)
        self.lbl_cam_val = ttk.Label(self.root, text="Camera", font=Constant_val_font)
        self.lbl_const_val = ttk.Label(self.root, text="Constant Values", font=Constant_val_font)
        self.lbl_data_visualization_val = ttk.Label(self.root, text="Data Visualization", font=Constant_val_font)

        """ open computer web camera """
        self.vid = cv2.VideoCapture(0)

        ''' Create a main window top color Label'''
        color_label = ttk.Label(self.root, background='blue', font=Main_label_font)
        color_label.place(relx=0.0, rely=0.0, relheight=0.1, relwidth=4)

        """ Canvas to encapsulate camera frame; 
            Create a canvas that can fit the above video source size         """
        self.canvas.place(relx=0.02, rely=0.21, relheight=0.42, relwidth=0.96)

        """ Label for constant changing values """
        ' Camera Label to hold the camera Label name '
        self.lbl_cam_val.place(relx=0.5, rely=0.15, relheight=0.05, relwidth=0.19)
        self.lbl_const_val.place(relx=0.7, rely=0.64, relheight=0.05, relwidth=0.22)
        self.lbl_data_visualization_val.place(relx=0.1, rely=0.64, relheight=0.05, relwidth=0.4)

        """ mainloop Exit Button"""

        self.exit_btn = ttk.Button(self.root, text="Exit", command=self.__del__)
        self.exit_btn.place(relx=0.75, rely=0.06, relheight=0.035, relwidth=0.13)

        ''' After this is called once, the update method will automatically be called every delay milliseconds '''

        self.delay = 15
        self.update()

        """ Graph Figure and data
            This graph will be improved to constantly show constant changing values
        """
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        ''' plotting Canvas. A tk.DrawingArea.'''
        gragh_plot = FigureCanvasTkAgg(fig, master=self.root)
        gragh_plot.draw()
        gragh_plot.get_tk_widget().place(relx=0.02, rely=0.7, relheight=0.28, relwidth=0.5)

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
            const_lbl.place(relx=0.67, rely=0.7, relheight=0.28, relwidth=0.3)

            if ret:
                ''' Return a boolean success flag and the current frame converted to BGR '''
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            else:
                return ret, None
        else:
            return None

    ' Release the video source when the object is destroyed '

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            self.root.destroy()


def main():
    """ Start Application """
    app = App()

    ''' Get screen width and height '''

    ws = app.root.winfo_screenwidth()  # width of the screen
    hs = app.root.winfo_screenheight()  # height of the screen

    app.root.geometry('%dx%d' % (ws, hs))
    app.root.mainloop()


if __name__ == '__main__':
    main()

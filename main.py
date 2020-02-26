# import the necessary packages
from camera import App
from imutils.video import VideoStream
import time

# Start Video Streams
vs = VideoStream(0).start()
time.sleep(2.0)

# start the app
pba = App(vs)

pba.root.mainloop()
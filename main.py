# import the necessary packages
from camera import App
from imutils.video import VideoStream
import time

# Start Video Streams
vidStreamer = VideoStream(0).start()
time.sleep(1.5)

# start the app
mainStart = App(vidStreamer)

mainStart.root.mainloop()

import kivy

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

# check what formats are supported for your targeted devices
# for example try h264 video and acc audo for android using an mp4
# container


class VideoPlayerApp(App):

    def build(self):
        return VideoPlayer(source= 'http://127.0.0.1:5000/feed', state='play')


if __name__ == '__main__':
    VideoPlayerApp().run()
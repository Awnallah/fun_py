"""A simple program that opens an entartaining video
for a given number of times every given number of minutes"""

import time
import webbrowser


def rest(minutes, times):
    """Opens a youtube video in the browser for a given
    number of times every given number of minutes """
    count = 1
    while count <= times:
        seconds = minutes * 60
        time.sleep(seconds)
        print (time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
        webbrowser.open("https://www.youtube.com/watch?v=gavT_q9CLME")
        count = count + 1


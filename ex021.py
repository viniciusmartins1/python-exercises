from pygame import mixer
mixer.init()
mixer.music.load('ex00021.mp3')
mixer.music.play()
input()
mixer.event.wait()





class my_song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_my_song(self):
        for words in self.lyrics:
            print words

bulls_on_parade = my_song(["They rally around tha family",
                        "With pockets full of shells"])


bulls_on_parade.sing_my_song()


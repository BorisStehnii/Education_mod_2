class Orchestra():

    def play(self):
        raise NotImplementedError("Error: no play method")

    def set_melody(self, new_melody):
        self._melody = new_melody

    def __add__(self, instrument):
        return self._melody + instrument._melody


class Piano(Orchestra):

    _melody = "____|||"

    def play(self):
        print(self._melody)


class Violin(Orchestra):

    _melody = "_|_|_|"

    def play(self):
        print(self._melody)


piano = Piano()
piano.play()
piano.set_melody("___||||___|")
piano.play()
violin = Violin()
violin.set_melody("|||||||||")
print(violin + piano, type(violin + piano))
violin_2 = Violin()
violin_2.set_melody("_|......")
print(violin + violin_2)

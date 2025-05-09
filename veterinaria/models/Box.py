class Box:
    def __init__(self, idBox):
        self.__idBox = idBox

    @property
    def idBox(self):
        return self.__idBox

    @idBox.setter
    def idBox(self, idBox):
        self.__idBox = idBox

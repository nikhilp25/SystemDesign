from TextMemento import TextMemento
class TextEditor:
    def __init__(self,text):
        self.__text= text
    
    def write(self,text):
        self.__text += text
    
    def get_text(self):
        return self.__text

    def save(self):
        return TextMemento(self.__text)

    def restore(self,tm):
        self.__text = tm.get_saved_text()
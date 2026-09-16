from TextMemento import TextMemento
class History:
    def __init__(self):
        self.__history = []

    def save_state(self, tm):
        self.__history.append(tm)
    
    def get_history(self):
        for i in range(len(self.__history)):
            print(f"{i}:{self.__history[i].get_saved_text()}")

    def undo(self):
        if(len(self.__history)>0):
            self.__history.pop()
            if(len(self.__history)==0):
                return TextMemento("")
            return self.__history[-1]
        else:
            return TextMemento("")
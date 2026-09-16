from History import History
from TextEditor import TextEditor


text_editor = TextEditor("")
history = History()

text_editor.write("Hello")
history.save_state(text_editor.save())
text_editor.write("Hello world")
history.save_state(text_editor.save())
text_editor.write("I'm goood")
history.save_state(text_editor.save())
text_editor.write("Possible")
history.save_state(text_editor.save())
print(history.get_history())
text_editor.restore(history.undo())
text_editor.write("ok It is possible")
history.save_state(text_editor.save())
print(history.get_history())
text_editor.write("Jello")
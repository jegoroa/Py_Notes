from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
 
import json
 
'''
notes = {"пельменная заметка (уже":{
    "text":"канал Максима the nistor",
    "tags":["youtube","Максим","letsplay","minecraft"]
}
}
'''
 
def read_file():
    with open("database.json","r",encoding="utf-8") as file:
        #json.dump(notes,file,ensure_ascii=False)
        notes = json.load(file)
    return notes
 
notes = read_file()
 
app = QApplication([])
main_w = QWidget()
main_w.setStyleSheet('background:grey')
main_w.setWindowIcon(QIcon("notes.png"))
main_w.setWindowTitle("Notes")


 
def to_exit():
    exit()
 
def show_note(): 
    note_name = getActualNoteName()
    text_w.setText(notes[note_name]["text"])
    tags_w.clear()
    tags_w.addItems(notes[note_name]["tags"])
 
def getActualNoteName():
    return names_w.selectedItems()[0].text()
 
def show_notes(data=notes):
    names_w.clear()
    tags_w.clear()
    text_w.clear()
    names_w.addItems(data) 
 
def save_note():
    note_name = getActualNoteName() #получаем имя выбранной заметки
    notes[note_name]["text"] = text_w.toPlainText() #достаем буквы из области
    #пишем их в заметку
    save_file()
 
#функция которая удаляет заметки
def del_note():
    note_name = getActualNoteName()
    del notes[note_name]
    show_notes()
    save_file()
 
def save_file(): #старый просто save
    with open("database.json","w",encoding="utf-8") as file:
        json.dump(notes,file,ensure_ascii=False)
 
def create_note():
    test = QInputDialog()
    test.setStyleSheet("background:white")

    
    #note_name, result = test.getText(main_w,"Нов. зам.","Название новой заметки")
    if result:
        notes[note_name] = {}
        notes[note_name]["text"] = ""
        notes[note_name]["tags"] = []
        show_notes()
        save_file()

def add_tag():
    note_name = getActualNoteName()
    tag = tag_input.text()
    notes[note_name]["tags"].append(tag)
    tags_w.clear()
    tags_w.addItems(notes[note_name]["tags"])
    tag_input.clear()
    save_file()

def del_tag():
    note_name = getActualNoteName()
    tag = tags_w.selectedItems()[0].text()
    notes[note_name]["tags"].remove(tag)
    tags_w.clear()
    tags_w.addItems(notes[note_name]["tags"])
    save_file()

def find_tag():
    pass 
    tag = tag_input.text()
    sorted = {}
    for note in notes:
        if tag in notes[note]["tags"]:
            sorted[note] = notes[note]
 
text_w = QTextEdit()
text_w.setStyleSheet("font-size:30px; background:lightgrey")
 
names_w = QListWidget()
names_w.setStyleSheet("background:lightgrey")
names_w.itemClicked.connect(show_note)

tags_w = QListWidget()
tags_w.setStyleSheet("background:lightgrey")

show_notes() #раньше был names_w.addItems(notes)  

 
create_btn = QPushButton("Создать") 
create_btn.clicked.connect(create_note) #tyt privazka
create_btn.setStyleSheet("background:green")

del_btn = QPushButton("Удалить заметку") 
del_btn.clicked.connect(del_note)
del_btn.setStyleSheet("background:red")

exit_btn = QPushButton("Выйти")
exit_btn.clicked.connect(to_exit)
exit_btn.setStyleSheet('background:red')

save_btn = QPushButton("Сохранить")
save_btn.clicked.connect(save_note)
save_btn.setStyleSheet("background:lightgrey")
 
tag_input = QLineEdit()
tag_input.setStyleSheet("background:lightgrey")

add_btn = QPushButton("Закрепить")
add_btn.clicked.connect(add_tag)
add_btn.setStyleSheet("background:green")

del_tag_btn = QPushButton("Открепить")
del_tag_btn.clicked.connect(del_tag)
del_tag_btn.setStyleSheet("background:red")

find_btn = QPushButton("Поиск")
#find_btn.clicked.connect(find_tag)
find_btn.setStyleSheet("background:lightgrey")
 
#зона создания линий
main = QHBoxLayout()
v_line = QVBoxLayout()
note_line = QHBoxLayout()
exit_line = QHBoxLayout()
tag_line = QHBoxLayout()
 
 
#зона обьединения всего со всем
main.addWidget(text_w)
main.addLayout(v_line)
 
v_line.addLayout(exit_line)
exit_line.addWidget(QLabel("Список заметок"))
exit_line.addWidget(exit_btn)
v_line.addWidget(names_w)
v_line.addLayout(note_line)
note_line.addWidget(create_btn)
note_line.addWidget(del_btn)
v_line.addWidget(save_btn)
v_line.addWidget(QLabel("Список Тегов"))
v_line.addWidget(tags_w)
v_line.addWidget(tag_input)
v_line.addLayout(tag_line)
tag_line.addWidget(add_btn)
tag_line.addWidget(del_tag_btn)
v_line.addWidget(find_btn)
main_w.setLayout(main)
 
#выйти alt + f4
main_w.showFullScreen()
app.exec()
#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
app=QApplication([])
win=QWidget()
win.resize(500,500)
win.setWindowTitle("ti clutoy")

class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Как будет привет по англиски", "Hello", "freddy fazber", "oni noni oni", "Oliver tri"))
question_list.append(Question("Как будет olive tri po angliski", "liverin", "fuzber", "oliber", "mister dep"))
question_list.append(Question("Как будет макдональдс по англиски", "jfdsfh", "mc donaldts", "BURGER KING", "boss KFC"))
question_list.append(Question("назови название часов", "6767", "FERRARI", "RED BULL", "CASIO"))















lineQV1=QVBoxLayout()
lineQV2=QVBoxLayout()
lineQH1=QHBoxLayout()

zapit=QLabel("Переклади на укр слово car")
answer1 = QRadioButton("Машина")
answer2 = QRadioButton("Автобус")
answer3 = QRadioButton("Корабель")
answer4 = QRadioButton("Потяг")
GroupBox = QGroupBox ("Назва")
Button=QPushButton("vidpovid")

radiogroup = QButtonGroup()
radiogroup.addButton(answer1)
radiogroup.addButton(answer2)
radiogroup.addButton(answer3)
radiogroup.addButton(answer4)

ResultGroupBox =  QGroupBox("Назва")
result = QLabel("Тут буде результат", alignment=Qt.AlignCenter)
correct =QLabel("ТУт буде правильна відповідь", alignment=Qt.AlignCenter)
result_lineQ1= QVBoxLayout()
result_lineQ1.addWidget(result, alignment=Qt.AlignCenter)
result_lineQ1.addWidget(correct, alignment=Qt.AlignCenter)
ResultGroupBox.setLayout(result_lineQ1)
ResultGroupBox.hide()


lineQV1.addWidget(answer1, alignment=Qt.AlignCenter)
lineQV2.addWidget(answer2, alignment=Qt.AlignCenter)
lineQV1.addWidget(answer3, alignment=Qt.AlignCenter)
lineQV2.addWidget(answer4, alignment=Qt.AlignCenter)

lineQH1.addLayout(lineQV1)
lineQH1.addLayout(lineQV2)
GroupBox.setLayout(lineQH1)

main_lineQH1=QHBoxLayout()
main_lineQH2=QHBoxLayout()
main_lineQH3=QHBoxLayout()

main_lineQH1.addWidget(zapit, alignment=Qt.AlignCenter)
main_lineQH2.addWidget(GroupBox, alignment=Qt.AlignCenter)
main_lineQH3.addWidget(Button, alignment=Qt.AlignCenter)

main_lineQV1 = QVBoxLayout()
main_lineQV1.addLayout(main_lineQH1)
main_lineQV1.addLayout(main_lineQH2)
main_lineQV1.addLayout(main_lineQH3)

win.setLayout(main_lineQV1)

def show_result():
    GroupBox.hide()
    ResultGroupBox.show()
    Button.setText("nastupne zapitanna")






def show_question():
    GroupBox.show()
    ResultGroupBox.hide()
    Button.setText("Otvet")

    radiogroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    radiogroup.setExclusive(True)

answers = [answer1, answer2, answer3, answer4]






def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    zapit.setText(q.text)
    correct.setText("Правильна відповідь:" + q.right_answer)
    show_question()

def right_wrong():

    win.total +=1
    if radiogroup.checkedButton() is None:
        return
    if answers[0].isChecked():
        result.setText("правильно")
        win.score +=1
    else:
        result.setText("Nevirno")
    show_result()
    rating = win.score/win.total * 100
    print("дано відповідей:", win.total)
    print("правильних відповідей:",win.score)
    print("uspishnisty:", rating, "%")

def next_question():
    random_question = randint(0, len(question_list) -1 )
    q = question_list[random_question]
    ask(q)





def button_OK():
    if Button.text() == "Otvet":
        right_wrong()
    else:
        next_question()
Button.clicked.connect(button_OK)
win.score = 0
win.total = 0
win.show()
app.exec_()




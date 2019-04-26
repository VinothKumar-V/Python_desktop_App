from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from datetime import datetime


class Agecollect(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QGridLayout()
        label_birth_date = QLabel("<b>Date of Birth</b>")
        self.line_birth_date = QLineEdit()
        label_name = QLabel("<b>Name</b>")
        self.line_edit_name = QLineEdit()
        self.lable_out = QLabel("")
        button = QPushButton("Calculate")
        self.checkbox = QCheckBox("Select If You Want Name to be Display")
        self.dropdown = QComboBox()
        self.dropdown.addItems(["Male", "Female"])
        self.lable_gender = QLabel("<b>Gender</b>")
        self.close_button = QPushButton("close")


        self.line_edit_name.setPlaceholderText("Type Your Name Here")
        self.line_birth_date.setPlaceholderText("MM/DD/YYYY")
        layout.addWidget(label_birth_date, 1, 0)
        layout.addWidget(self.line_birth_date, 1, 1)
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.line_edit_name,  0, 1)
        layout.addWidget(self.lable_gender, 2, 0)
        layout.addWidget(self.dropdown, 2, 1)
        layout.addWidget(self.checkbox, 3, 1)
        layout.addWidget(self.close_button, 4, 0)
        layout.addWidget(button, 4, 1)



        self.setLayout(layout)
        self.setWindowTitle("JPMC Shelden")
        self.setFocus()
        self.close_button.clicked.connect(self.close)
        button.clicked.connect(self.days_cal)
        #line_birth_date.textEdited.connect(self.days_cal)

    def update_out(self, text):
        text_final = "Hi {0}...".format(text)
        self.lable_out.setText(text_final)

    def days_cal(self):
        date_format = "%m/%d/%Y"
        birth_date_frm = datetime.strptime(self.line_birth_date.text(), date_format)
        current_date = datetime.strptime(datetime.now().strftime(date_format), date_format)
        delta = current_date - birth_date_frm
        if self.checkbox.isChecked():
            out = "Hi {0} Your Total Number of Days {1}".format(self.line_edit_name.text(), delta.days)
        else:
            out = "Hi Your Total Number of Days {0}".format( delta.days)

        #self.lable_out.setText(out)

        QMessageBox.information(self, "Information", out)
        self.line_edit_name.setText("")
        self.line_birth_date.setText("")









app = QApplication(sys.argv)
app.setApplicationName('Days Calculator')
dialog = Agecollect()
dialog.show()
app.exec_()
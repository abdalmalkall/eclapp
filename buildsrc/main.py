import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox,
    QStackedWidget, QGraphicsOpacityEffect
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QFont, QCursor, QDesktopServices
from PyQt5.QtCore import QUrl

class RoleSelectionWidget(QWidget):
    def __init__(self, switch_to_login):
        super().__init__()
        self.switch_to_login = switch_to_login
        self.setStyleSheet("background-color: #1a1b26; color: #c0caf5; font-family: 'Segoe UI';")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 50, 40, 50)
        layout.setSpacing(30)

        title = QLabel("Welcome to EduNova AI")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setStyleSheet("color: #7aa2f7;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        label = QLabel("Who are you?")
        label.setFont(QFont("Segoe UI", 14))
        layout.addWidget(label, alignment=Qt.AlignCenter)

        btn_student = QPushButton("Login as Student")
        btn_teacher = QPushButton("Login as Teacher")

        for btn in (btn_student, btn_teacher):
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #7aa2f7;
                    border-radius: 10px;
                    font-size: 16pt;
                    padding: 12px;
                    color: #1a1b26;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #5a8def;
                }
            """)

        btn_student.clicked.connect(lambda: self.switch_to_login('student'))
        btn_teacher.clicked.connect(lambda: self.switch_to_login('teacher'))

        layout.addWidget(btn_student)
        layout.addWidget(btn_teacher)

        # Instagram and creator
        footer_layout = QHBoxLayout()
        creator_label = QLabel("Created by محمد مجدي وفيق ياسين")
        creator_label.setStyleSheet("color: #7aa2f7; font-size: 11pt;")
        footer_layout.addWidget(creator_label)

        insta_btn = QPushButton("Instagram")
        insta_btn.setCursor(QCursor(Qt.PointingHandCursor))
        insta_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #7aa2f7;
                font-size: 11pt;
                border: none;
                text-decoration: underline;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #5a8def;
            }
        """)
        insta_btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://www.instagram.com/skakashi_10/")))
        footer_layout.addWidget(insta_btn)

        layout.addLayout(footer_layout)
        self.setLayout(layout)

class LoginFormWidget(QWidget):
    def __init__(self, role, back_to_selection):
        super().__init__()
        self.role = role
        self.back_to_selection = back_to_selection
        self.setStyleSheet("background-color: #1a1b26; color: #c0caf5; font-family: 'Segoe UI';")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(15)

        title = QLabel(f"{self.role.capitalize()} Login")
        title.setStyleSheet("color: #7aa2f7;")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Gender combo box
        label_gender = QLabel("Gender:")
        label_gender.setFont(QFont("Segoe UI", 13))
        layout.addWidget(label_gender)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female"])
        self.gender_combo.setStyleSheet("""
            QComboBox {
                background-color: #2e2f3e;
                border: 1px solid #44475a;
                border-radius: 6px;
                padding: 6px;
                font-size: 13pt;
                color: white;
            }
            QComboBox:hover { border-color: #7aa2f7; }
            QComboBox::drop-down {
                border: none;
            }
        """)
        layout.addWidget(self.gender_combo)

        # Course combo box with given courses
        label_course = QLabel("Course:")
        label_course.setFont(QFont("Segoe UI", 13))
        layout.addWidget(label_course)

        courses = [
            "Applied Science (Extended Certificate)",
            "Computing (Extended Certificate)",
            "Construction and the Built Environment (Extended Certificate)",
            "Early Childhood Development (Extended Certificate)",
            "Engineering (Extended Certificate)",
            "Health and Social Care (Extended Certificate)",
            "Information Technology (Extended Certificate)",
            "Medical Science (Extended Certificate)"
        ]
        self.course_combo = QComboBox()
        self.course_combo.addItems(courses)
        self.course_combo.setStyleSheet("""
            QComboBox {
                background-color: #2e2f3e;
                border: 1px solid #44475a;
                border-radius: 6px;
                padding: 6px;
                font-size: 13pt;
                color: white;
            }
            QComboBox:hover { border-color: #7aa2f7; }
            QComboBox::drop-down {
                border: none;
            }
        """)
        layout.addWidget(self.course_combo)

        # Email input
        label_email = QLabel("Email:")
        label_email.setFont(QFont("Segoe UI", 13))
        layout.addWidget(label_email)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("example@jolearn.jo")
        self.email_input.setStyleSheet("""
            background-color: #2e2f3e;
            border: 1px solid #44475a;
            border-radius: 6px;
            padding: 10px;
            color: white;
            font-size: 13pt;
        """)
        layout.addWidget(self.email_input)

        # Password input
        label_pass = QLabel("Password:")
        label_pass.setFont(QFont("Segoe UI", 13))
        layout.addWidget(label_pass)

        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.setStyleSheet("""
            background-color: #2e2f3e;
            border: 1px solid #44475a;
            border-radius: 6px;
            padding: 10px;
            color: white;
            font-size: 13pt;
        """)
        layout.addWidget(self.pass_input)

        # Buttons layout
        btn_layout = QHBoxLayout()

        self.back_btn = QPushButton("Back")
        self.back_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: #44475a;
                border-radius: 10px;
                font-size: 14pt;
                padding: 10px;
                color: #c0caf5;
            }
            QPushButton:hover {
                background-color: #5a5f78;
            }
        """)
        self.back_btn.clicked.connect(self.back_to_selection)
        btn_layout.addWidget(self.back_btn)

        self.login_btn = QPushButton("Login")
        self.login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #7aa2f7;
                border-radius: 10px;
                font-size: 16pt;
                padding: 10px;
                color: #1a1b26;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a8def;
            }
        """)
        self.login_btn.clicked.connect(self.handle_login)
        btn_layout.addWidget(self.login_btn)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def handle_login(self):
        email = self.email_input.text().strip()
        password = self.pass_input.text().strip()
        gender = self.gender_combo.currentText()
        course = self.course_combo.currentText()

        if not email.endswith("@jolearn.jo"):
            QMessageBox.warning(self, "Error", "Email must end with @jolearn.jo")
            return
        if not password:
            QMessageBox.warning(self, "Error", "Password cannot be empty")
            return

        QMessageBox.information(
            self,
            "Welcome",
            f"Welcome {self.role.capitalize()} ({gender}), Course: {course}\nEmail: {email}"
        )

    def back_to_selection(self):
        self.back_to_selection()


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EduNova AI Login")
        self.resize(480, 580)
        self.setStyleSheet("background-color: #1a1b26;")

        self.role_selection = RoleSelectionWidget(self.switch_to_login)
        self.addWidget(self.role_selection)

        self.login_student = LoginFormWidget("student", self.back_to_selection)
        self.addWidget(self.login_student)

        self.login_teacher = LoginFormWidget("teacher", self.back_to_selection)
        self.addWidget(self.login_teacher)

        self.setCurrentWidget(self.role_selection)

    def slide_to_widget(self, widget):
        current_index = self.currentIndex()
        new_index = self.indexOf(widget)
        if current_index == new_index:
            return

        direction = 1 if new_index > current_index else -1

        current_widget = self.currentWidget()
        next_widget = widget

        width = self.frameRect().width()

        next_widget.setGeometry(0, 0, width, self.frameRect().height())
        next_widget.move(direction * width, 0)
        next_widget.show()

        anim_current = QPropertyAnimation(current_widget, b"pos", self)
        anim_current.setDuration(400)
        anim_current.setStartValue(current_widget.pos())
        anim_current.setEndValue(current_widget.pos() - QPoint(direction * width, 0))
        anim_current.setEasingCurve(QEasingCurve.InOutQuad)

        anim_next = QPropertyAnimation(next_widget, b"pos", self)
        anim_next.setDuration(400)
        anim_next.setStartValue(next_widget.pos())
        anim_next.setEndValue(QPoint(0, 0))
        anim_next.setEasingCurve(QEasingCurve.InOutQuad)

        def on_animation_finished():
            self.setCurrentWidget(next_widget)
            current_widget.hide()

        anim_next.finished.connect(on_animation_finished)
        anim_current.start()
        anim_next.start()

    def switch_to_login(self, role):
        if role == 'student':
            self.slide_to_widget(self.login_student)
        else:
            self.slide_to_widget(self.login_teacher)

    def back_to_selection(self):
        self.slide_to_widget(self.role_selection)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 
    import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    import sys

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import QStackedWidget
from user import UserApp
from employee import EmployeeApp

class MainApp(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # ตั้งค่า UI พื้นฐาน
        self.setWindowTitle('Marumthuy Booking System')
        self.setGeometry(100, 100, 300, 200)

        # สร้าง Layout และปุ่มสำหรับเลือกบทบาท
        layout = QVBoxLayout()

        label = QLabel('กรุณาเลือกบทบาทของคุณ:')
        layout.addWidget(label)

        user_button = QPushButton('User')
        user_button.clicked.connect(self.open_user_window)
        layout.addWidget(user_button)

        employee_button = QPushButton('Employee')
        employee_button.clicked.connect(self.open_employee_window)
        layout.addWidget(employee_button)

        self.setLayout(layout)

    def open_user_window(self):
        # แสดงหน้าต่าง User
        self.stacked_widget.setCurrentWidget(self.stacked_widget.user_app)

    def open_employee_window(self):
        # แสดงหน้าต่าง Employee
        self.stacked_widget.setCurrentWidget(self.stacked_widget.employee_app)

class BookingSystemUI(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # สร้างหน้าต่างหลักและ UI ของแต่ละบทบาท
        self.main_app = MainApp(self)
        self.user_app = UserApp()
        self.employee_app = EmployeeApp()

        # เพิ่มหน้าต่างแต่ละหน้าเข้าไปใน QStackedWidget
        self.addWidget(self.main_app)
        self.addWidget(self.user_app)
        self.addWidget(self.employee_app)

        # เชื่อมปุ่มย้อนกลับใน UserApp และ EmployeeApp กลับไปยัง MainApp
        self.user_app.close = self.show_main_app
        self.employee_app.close = self.show_main_app

        # ตั้งค่าเริ่มต้นให้แสดงหน้าต่างหลัก
        self.setCurrentWidget(self.main_app)

    def show_main_app(self):
        # แสดงหน้าต่างหลัก
        self.setCurrentWidget(self.main_app)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    booking_system_ui = BookingSystemUI()
    booking_system_ui.setWindowTitle('Marumthuy Booking System')
    booking_system_ui.setGeometry(100, 100, 400, 600)  # ขนาดเท่าหน้าจอโทรศัพท์
    booking_system_ui.show()
    sys.exit(app.exec_())
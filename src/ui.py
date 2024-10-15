import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from main import MainApp
from user import UserApp
from employee import EmployeeApp

class BookingSystemUI(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # สร้างหน้าต่างหลักและ UI ของแต่ละบทบาท
        self.main_app = MainApp()
        self.user_app = UserApp()
        self.employee_app = EmployeeApp()

        # เพิ่มหน้าต่างแต่ละหน้าเข้าไปใน QStackedWidget
        self.addWidget(self.main_app)
        self.addWidget(self.user_app)
        self.addWidget(self.employee_app)

        # เชื่อมปุ่มจาก MainApp ไปยังหน้าต่าง User และ Employee
        self.main_app.open_user_window = self.show_user_app
        self.main_app.open_employee_window = self.show_employee_app

        # ตั้งค่าเริ่มต้นให้แสดงหน้าต่างหลัก
        self.setCurrentWidget(self.main_app)

    def show_user_app(self):
        # แสดงหน้าต่างสำหรับ User
        self.setCurrentWidget(self.user_app)

    def show_employee_app(self):
        # แสดงหน้าต่างสำหรับ Employee
        self.setCurrentWidget(self.employee_app)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    booking_system_ui = BookingSystemUI()
    booking_system_ui.setWindowTitle('Marumthuy Booking System')
    booking_system_ui.setGeometry(100, 100, 400, 600)  # ขนาดเท่าหน้าจอโทรศัพท์
    booking_system_ui.show()
    sys.exit(app.exec_())
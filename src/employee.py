import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QInputDialog, QLineEdit, QDialog, QFormLayout, QStackedWidget, QMessageBox
from PyQt5.QtCore import Qt
import utils
import users_data_handler

class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('กรุณาใส่รหัสผ่าน')
        self.setGeometry(100, 100, 300, 150)
        layout = QFormLayout()

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addRow('รหัสผ่าน:', self.password_input)

        submit_button = QPushButton('ตกลง')
        submit_button.clicked.connect(self.check_password)
        layout.addRow(submit_button)

        self.setLayout(layout)

    def check_password(self):
        if self.password_input.text() == '123456':
            self.accept()
        else:
            self.reject()

class EmployeeApp(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()
        self.load_bookings_from_json()

    def initUI(self):
        # ตั้งค่า UI พื้นฐาน
        self.setWindowTitle('Marumthuy Booking System - Employee')
        self.setGeometry(100, 100, 600, 400)

        # สร้าง Layout และองค์ประกอบต่างๆ สำหรับการจัดการคิว
        layout = QVBoxLayout()

        label = QLabel('รายการการจองทั้งหมด:')
        layout.addWidget(label)

        # แสดงรายการการจองในรูปแบบตาราง
        self.booking_table = QTableWidget()
        self.booking_table.setColumnCount(5)
        self.booking_table.setHorizontalHeaderLabels(['เลขคิว', 'ชื่อ', 'วันที่', 'เวลา', 'สถานะ'])
        self.booking_table.verticalHeader().setVisible(False)
        self.booking_table.setSelectionBehavior(QTableWidget.SelectRows)  # คลุมสีทั้งแถวเมื่อเลือก
        self.booking_table.setSelectionMode(QTableWidget.SingleSelection)  # เลือกได้ทีละแถวเท่านั้น
        layout.addWidget(self.booking_table)

        # ปุ่มเปลี่ยนสถานะการจอง
        manage_button = QPushButton('จัดการคิว')
        manage_button.clicked.connect(self.manage_booking)
        layout.addWidget(manage_button)

        # ปุ่มย้อนกลับ
        back_button = QPushButton('ย้อนกลับ')
        back_button.clicked.connect(self.go_back_to_main)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def load_bookings(self, bookings):
        # ฟังก์ชันโหลดข้อมูลการจองลงใน QTableWidget
        self.booking_table.setRowCount(len(bookings))
        for row, booking in enumerate(bookings):
            self.booking_table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.booking_table.setItem(row, 1, QTableWidgetItem(booking['name']))
            self.booking_table.setItem(row, 2, QTableWidgetItem(booking['date']))
            self.booking_table.setItem(row, 3, QTableWidgetItem(booking['time']))
            self.booking_table.setItem(row, 4, QTableWidgetItem(booking['status']))

    def load_bookings_from_json(self):
        # โหลดข้อมูลการจองจากไฟล์ JSON และแสดงใน QTableWidget
        bookings = utils.load_bookings()
        self.load_bookings(bookings)

    def manage_booking(self):
        # ฟังก์ชันจัดการการจอง
        current_row = self.booking_table.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, 'ข้อผิดพลาด', 'กรุณาเลือกคิวที่ต้องการจัดการ')
            return

        options = ["กำลังให้บริการ", "สำเร็จ", "ยกเลิก"]
        status, ok = QInputDialog.getItem(self, "เปลี่ยนสถานะการจอง", "เลือกสถานะใหม่: ", options, 0, False)
        if ok and status:
            # อัพเดทสถานะการจองในไฟล์ booking_data.json
            bookings = utils.load_bookings()
            booking = bookings[current_row]
            if status == "กำลังให้บริการ":
                booking['status'] = status
                QMessageBox.information(self, 'สถานะการจอง', 'การจองถูกเปลี่ยนสถานะเป็นกำลังให้บริการแล้ว')
            elif status in ["สำเร็จ", "ยกเลิก"]:
                # บันทึกสถานะที่ถูกยกเลิกและสำเร็จในไฟล์ users_data.json ก่อนที่จะลบออกจาก booking_data.json
                users_data_handler.add_user_status(booking['name'], booking['date'], booking['time'], booking['phone'], status)
                bookings.pop(current_row)
                QMessageBox.information(self, 'สถานะการจอง', 'การจองถูกลบออกเรียบร้อยแล้ว')
            utils.save_bookings(bookings)
            self.load_bookings_from_json()

    def go_back_to_main(self):
        # กลับไปยังหน้าต่างหลัก (MainApp)
        self.stacked_widget.setCurrentWidget(self.stacked_widget.main_app)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_dialog = PasswordDialog()
    if password_dialog.exec_() == QDialog.Accepted:
        stacked_widget = QStackedWidget()
        employee_app = EmployeeApp(stacked_widget)
        stacked_widget.addWidget(employee_app)
        stacked_widget.setCurrentWidget(employee_app)
        stacked_widget.setWindowTitle('Marumthuy Booking System - Employee')
        stacked_widget.setGeometry(100, 100, 600, 600)  # ขนาดเท่าหน้าจอโทรศัพท์
        stacked_widget.show()
        sys.exit(app.exec_())
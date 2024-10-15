import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton
from PyQt5.QtCore import QDate

class UserApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ตั้งค่า UI พื้นฐาน
        self.setWindowTitle('Marumthuy Booking System - User')
        self.setGeometry(100, 100, 400, 300)

        # สร้าง Layout และองค์ประกอบต่างๆ สำหรับการจองคิว
        layout = QVBoxLayout()

        label = QLabel('กรุณากรอกข้อมูลการจอง:')
        layout.addWidget(label)

        # ช่องกรอกชื่อ
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('ชื่อของคุณ')
        layout.addWidget(self.name_input)

        # เลือกวันที่ (ค่าเริ่มต้นเป็นวันที่ปัจจุบัน)
        self.date_combo = QComboBox()
        self.date_combo.addItem(QDate.currentDate().toString("dd/MM/yyyy"))
        layout.addWidget(self.date_combo)

        # เลือกเวลา (ตัวอย่าง dropdown)
        self.time_combo = QComboBox()
        self.time_combo.addItems(['09:00', '10:00', '11:00', '13:00', '14:00', '15:00'])
        layout.addWidget(self.time_combo)

        # ช่องกรอกจำนวนคน
        self.people_input = QLineEdit()
        self.people_input.setPlaceholderText('จำนวนคน')
        layout.addWidget(self.people_input)

        # ช่องกรอกเบอร์โทรศัพท์
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText('เบอร์โทรศัพท์')
        layout.addWidget(self.phone_input)

        # ปุ่มส่งข้อมูลการจอง
        submit_button = QPushButton('ส่งข้อมูลการจอง')
        submit_button.clicked.connect(self.submit_booking)
        layout.addWidget(submit_button)

        # ปุ่มย้อนกลับ
        back_button = QPushButton('ย้อนกลับ')
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def submit_booking(self):
        # ฟังก์ชันสำหรับการส่งข้อมูลการจอง (เตรียมเชื่อมต่อกับ utils.py ในภายหลัง)
        name = self.name_input.text()
        date = self.date_combo.currentText()
        time = self.time_combo.currentText()
        people = self.people_input.text()
        phone = self.phone_input.text()
        
        # แสดงข้อมูลที่กรอกใน console (เตรียมบันทึกในไฟล์ booking_data.json)
        print(f"Name: {name}, Date: {date}, Time: {time}, People: {people}, Phone: {phone}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_app = UserApp()
    user_app.show()
    sys.exit(app.exec_())
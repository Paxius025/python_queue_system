import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QInputDialog

class EmployeeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ตั้งค่า UI พื้นฐาน
        self.setWindowTitle('Marumthuy Booking System - Employee')
        self.setGeometry(100, 100, 400, 400)

        # สร้าง Layout และองค์ประกอบต่างๆ สำหรับการจัดการคิว
        layout = QVBoxLayout()

        label = QLabel('รายการการจองทั้งหมด:')
        layout.addWidget(label)

        # แสดงรายการการจอง
        self.booking_list = QListWidget()
        layout.addWidget(self.booking_list)

        # ปุ่มเปลี่ยนสถานะการจอง
        manage_button = QPushButton('จัดการคิว')
        manage_button.clicked.connect(self.manage_booking)
        layout.addWidget(manage_button)

        # ปุ่มย้อนกลับ
        back_button = QPushButton('ย้อนกลับ')
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def load_bookings(self, bookings):
        # ฟังก์ชันโหลดข้อมูลการจองลงใน QListWidget (เชื่อมต่อกับ utils.py ในภายหลัง)
        self.booking_list.clear()
        for booking in bookings:
            self.booking_list.addItem(f"ชื่อ: {booking['name']}, วันที่: {booking['date']}, เวลา: {booking['time']}")

    def manage_booking(self):
        # ฟังก์ชันจัดการการจอง (เชื่อมต่อกับ utils.py ในภายหลัง)
        current_item = self.booking_list.currentItem()
        if current_item:
            options = ["กำลังให้บริการ", "สำเร็จ", "ยกเลิก"]
            status, ok = QInputDialog.getItem(self, "เปลี่ยนสถานะการจอง", "เลือกสถานะใหม่: ", options, 0, False)
            if ok and status:
                print(f"การจอง: {current_item.text()} เปลี่ยนสถานะเป็น: {status}")
                # เตรียมการจัดการข้อมูลในไฟล์ booking_data.json ในภายหลัง

if __name__ == '__main__':
    app = QApplication(sys.argv)
    employee_app = EmployeeApp()
    employee_app.show()
    sys.exit(app.exec_())
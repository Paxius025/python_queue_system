import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QLineEdit, QComboBox, QMessageBox
from PyQt5.QtCore import QDate
import utils

class UserApp(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # ตั้งค่า UI พื้นฐาน
        self.setWindowTitle('Marumthuy Booking System - User')
        self.setGeometry(100, 100, 400, 300)

        # สร้าง Layout และองค์ประกอบต่างๆ สำหรับหน้าหลักของ User
        layout = QVBoxLayout()

        label = QLabel('กรุณาเลือกการทำงานที่ต้องการ:')
        layout.addWidget(label)

        # ปุ่มสำหรับจองคิว
        book_button = QPushButton('จองคิว')
        book_button.clicked.connect(self.open_booking_page)
        layout.addWidget(book_button)

        # ปุ่มสำหรับดูคิว
        view_queue_button = QPushButton('ดูคิวของคุณ')
        view_queue_button.clicked.connect(self.open_queue_page)
        layout.addWidget(view_queue_button)

        # ปุ่มย้อนกลับ
        back_button = QPushButton('ย้อนกลับ')
        back_button.clicked.connect(self.stacked_widget.show_main_app)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def open_booking_page(self):
        # แสดงหน้าจองคิว
        self.stacked_widget.booking_page.reset_inputs()
        self.stacked_widget.setCurrentWidget(self.stacked_widget.booking_page)

    def open_queue_page(self):
        # แสดงหน้าดูคิว
        self.stacked_widget.queue_page.reset_inputs()
        self.stacked_widget.setCurrentWidget(self.stacked_widget.queue_page)

class BookingPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # ตั้งค่า UI พื้นฐาน
        self.setWindowTitle('Marumthuy Booking System - Booking')
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
        self.time_combo.addItems(['09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00'])
        layout.addWidget(self.time_combo)

        # ช่องกรอกจำนวนคน
        self.people_combo = QComboBox()
        self.people_combo.addItems(['1', '2', '3', '4', '5', '6'])
        layout.addWidget(self.people_combo)

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
        back_button.clicked.connect(self.stacked_widget.show_user_app)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def reset_inputs(self):
        # รีเซตข้อมูลในช่องกรอกข้อมูล
        self.name_input.clear()
        self.date_combo.setCurrentIndex(0)
        self.time_combo.setCurrentIndex(0)
        self.people_combo.setCurrentIndex(0)
        self.phone_input.clear()

    def submit_booking(self):
        # ฟังก์ชันสำหรับการส่งข้อมูลการจองไปยังไฟล์ booking_data.json
        name = self.name_input.text()
        date = self.date_combo.currentText()
        time = self.time_combo.currentText()
        people = self.people_combo.currentText()
        phone = self.phone_input.text()

        # ตรวจสอบว่าช่องกรอกข้อมูลครบถ้วนหรือไม่
        if not name or not phone:
            QMessageBox.warning(self, 'ข้อมูลไม่ครบถ้วน', 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return

        # ตรวจสอบความยาวของชื่อและเบอร์โทรศัพท์
        if len(name) < 5:
            QMessageBox.warning(self, 'ข้อมูลไม่ถูกต้อง', 'กรุณากรอกชื่อที่มีความยาวอย่างน้อย 5 ตัวอักษร')
            return

        if len(phone) != 10 or not phone.isdigit():
            QMessageBox.warning(self, 'ข้อมูลไม่ถูกต้อง', 'กรุณากรอกเบอร์โทรศัพท์ที่มีความยาว 10 ตัวเลข')
            return

        # ตรวจสอบว่าเบอร์โทรศัพท์ซ้ำหรือไม่
        bookings = utils.load_bookings()
        for booking in bookings:
            if booking['phone'] == phone:
                QMessageBox.warning(self, 'การจองซ้ำ', 'คุณได้ใช้เบอร์นี้จองไปแล้ว')
                return

        # บันทึกข้อมูลการจองลงในไฟล์ booking_data.json
        utils.add_booking(name, date, time, people, phone, status='จองแล้ว')

        # แสดงข้อความยืนยันเมื่อการจองเสร็จสิ้น
        QMessageBox.information(self, 'สำเร็จ', 'การจองของคุณถูกบันทึกเรียบร้อยแล้ว')

class QueuePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # ตั้งค่า UI พื้นฐาน
        self.setWindowTitle('Marumthuy Booking System - Queue')
        self.setGeometry(100, 100, 400, 300)

        # สร้าง Layout และองค์ประกอบต่างๆ สำหรับการดูคิว
        layout = QVBoxLayout()

        label = QLabel('ดูคิวของคุณ:')
        layout.addWidget(label)

        # ช่องกรอกเบอร์โทรศัพท์เพื่อค้นหาคิวของตัวเอง
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText('กรอกเบอร์โทรศัพท์ของคุณ')
        layout.addWidget(self.phone_input)

        # ปุ่มค้นหาคิว
        search_button = QPushButton('ค้นหาคิว')
        search_button.clicked.connect(self.search_queue)
        layout.addWidget(search_button)

        # แสดงผลการค้นหา
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        # ปุ่มย้อนกลับ
        back_button = QPushButton('ย้อนกลับ')
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.stacked_widget.user_app))
        layout.addWidget(back_button)

        self.setLayout(layout)

    def reset_inputs(self):
        # รีเซตข้อมูลในช่องกรอกข้อมูล
        self.phone_input.clear()
        self.result_label.setText('')

    def search_queue(self):
        # ฟังก์ชันค้นหาคิวจากเบอร์โทรศัพท์
        phone = self.phone_input.text()
        bookings = utils.load_bookings()
        filtered_bookings = [booking for booking in bookings if booking['phone'] == phone]
        if filtered_bookings:
            result_texts = []
            for booking in filtered_bookings:
                queue_number = bookings.index(booking) + 1  # หาเลขคิวโดยใช้ตำแหน่งในรายการ
                result_texts.append(f"ชื่อ: {booking['name']}, วันที่: {booking['date']}, เวลา: {booking['time']}, สถานะ: {booking['status']}, คิวที่: {queue_number}")
            result_text = '\n'.join(result_texts)
            self.result_label.setText(result_text)
        else:
            self.result_label.setText('ไม่พบข้อมูลการจองของคุณ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    user_app = UserApp(stacked_widget)
    booking_page = BookingPage(stacked_widget)
    queue_page = QueuePage(stacked_widget)

    stacked_widget.user_app = user_app
    stacked_widget.booking_page = booking_page
    stacked_widget.queue_page = queue_page

    stacked_widget.addWidget(user_app)
    stacked_widget.addWidget(booking_page)
    stacked_widget.addWidget(queue_page)

    stacked_widget.setWindowTitle('Marumthuy Booking System')
    stacked_widget.setGeometry(100, 100, 400, 600)  # ขนาดเท่าหน้าจอโทรศัพท์
    stacked_widget.setCurrentWidget(user_app)
    stacked_widget.show()

    sys.exit(app.exec_())
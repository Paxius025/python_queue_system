import json

BOOKING_FILE = 'booking_data.json'

def load_bookings():
    """
    ฟังก์ชันโหลดข้อมูลการจองจากไฟล์ JSON
    """
    try:
        with open(BOOKING_FILE, 'r', encoding='utf-8') as file:
            bookings = json.load(file)
            return bookings
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_bookings(bookings):
    """
    ฟังก์ชันบันทึกข้อมูลการจองลงในไฟล์ JSON
    """
    with open(BOOKING_FILE, 'w', encoding='utf-8') as file:
        json.dump(bookings, file, ensure_ascii=False, indent=4)

def add_booking(name, date, time, people, phone, status='จองแล้ว'):
    """
    ฟังก์ชันเพิ่มการจองใหม่ลงในไฟล์ JSON
    """
    bookings = load_bookings()
    new_booking = {
        'name': name,
        'date': date,
        'time': time,
        'people': people,
        'phone': phone,
        'status': status
    }
    bookings.append(new_booking)
    save_bookings(bookings)

def update_booking_status(index, new_status):
    """
    ฟังก์ชันเปลี่ยนสถานะการจอง
    """
    bookings = load_bookings()
    if 0 <= index < len(bookings):
        bookings[index]['status'] = new_status
        if new_status in ['สำเร็จ', 'ยกเลิก']:
            # ลบการจองที่สถานะเป็น 'สำเร็จ' หรือ 'ยกเลิก'
            bookings.pop(index)
        save_bookings(bookings)

def find_booking_by_phone(phone):
    """
    ฟังก์ชันค้นหาการจองโดยเบอร์โทรศัพท์
    """
    bookings = load_bookings()
    return [booking for booking in bookings if booking['phone'] == phone]

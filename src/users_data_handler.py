import json

USERS_FILE = 'users_data.json'

def load_users_data():
    """
    ฟังก์ชันโหลดข้อมูลผู้ใช้จากไฟล์ JSON
    """
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as file:
            users_data = json.load(file)
            return users_data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_users_data(users_data):
    """
    ฟังก์ชันบันทึกข้อมูลผู้ใช้ลงในไฟล์ JSON
    """
    with open(USERS_FILE, 'w', encoding='utf-8') as file:
        json.dump(users_data, file, ensure_ascii=False, indent=4)

def add_user_status(name, date, time, phone, status):
    """
    ฟังก์ชันเพิ่มสถานะของผู้ใช้ใหม่ลงในไฟล์ JSON
    """
    users_data = load_users_data()
    new_user_status = {
        'name': name,
        'date': date,
        'time': time,
        'phone': phone,
        'status': status
    }
    users_data.append(new_user_status)
    save_users_data(users_data)
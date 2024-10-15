# PuppyQueue Booking System 🗓️✨

PuppyQueue is a ticket booking system designed to manage and streamline the queue process for both users and employees. The system allows users to book appointments, check queue statuses, and enables employees to manage customer queues efficiently.

## Features 🚀
- **User Booking Interface**: Users can book appointments through an intuitive UI and check the status of their bookings.
- **Employee Management Interface**: Employees can view and manage user bookings in real-time.
- **Queue Management**: System maintains a shared queue and provides real-time updates for users and employees.
- **Easy Navigation**: Each interface features a "Back" button for ease of use and navigation.

## Project Structure 🗂️
```
Marumthuy_booking_system/
├── env/
├── requirements.txt
└── src/
    ├── main.py
    ├── utils.py
    ├── ui.py
    ├── booking_data.json
    └── ui/
        ├── booking_options.py       # UI for choosing booking options (book or check queue)
        ├── user_page/
            ├── user_app.py          # User booking interface
            └── user_queue.py        # User queue status interface
        └── employee_app.py          # Employee management interface
```

## Installation 🛠️
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Marumthuy_booking_system.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Marumthuy_booking_system
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 📋
1. **Run the main application**:
   ```bash
   python src/main.py
   ```

2. **Navigate through the options to book or check appointments**:
   - Users can book a ticket or check their queue status.
   - Employees can manage customer queues.

## Requirements 📦
- **Python 3.8+**
- **PyQt5** (for User Interface)
- Other dependencies are listed in `requirements.txt`

## Development 🔧
The project consists of multiple modules:
- **main.py**: Entry point of the application that handles launching user and employee interfaces.
- **utils.py**: Contains utility functions, such as reading/writing JSON files for booking data.
- **ui.py**: Implements the user interface using PyQt5, featuring dropdown selections for roles, time, and date.
- **booking_options.py**: Provides booking options for users to either book an appointment or check the queue.
- **user_app.py / user_queue.py**: Handles user-related actions, such as booking appointments and viewing queues.
- **employee_app.py**: Allows employees to view and manage customer appointments.

## Contributing 🤝
Contributions are welcome! Please create an issue or submit a pull request if you'd like to contribute.

1. **Fork the repository**
2. **Create your feature branch** (`git checkout -b feature/new-feature`)
3. **Commit your changes** (`git commit -m 'Add some feature'`)
4. **Push to the branch** (`git push origin feature/new-feature`)
5. **Create a new Pull Request**

## License 📜
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Feel free to contribute, suggest improvements, or report any issues! 😊

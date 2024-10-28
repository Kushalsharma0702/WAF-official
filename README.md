# Web Application Firewall (WAF)


## Table of Contents

- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Stats](#stats)

## Description

The **Web Application Firewall (WAF)** is a powerful tool designed to protect web applications from various types of attacks, such as SQL injection and cross-site scripting (XSS). This application provides an intuitive admin interface for managing security rules, making it easier to enhance the safety of your applications.

## Features

- **Rule Management:** Easily add, delete, and view security rules.
- **Request Filtering:** Automatically blocks harmful requests based on your defined rules.
- **Logging:** Records all blocked requests for auditing and analysis.
- **Responsive Design:** Optimized for both desktop and mobile devices.

## Technologies Used

- **Python** - Backend development
- **Flask** - Web framework
- **SQLAlchemy** - ORM for database interactions
- **SQLite** - Lightweight database
- **HTML/CSS** - Frontend design

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/waf_project.git
   cd waf_project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

## Usage

- Access the WAF at `http://127.0.0.1:5000/`.
- Navigate to the admin panel to manage your security rules.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make your changes and commit:**
   ```bash
   git commit -m "Add some feature"
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Create a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

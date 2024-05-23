
# 🌱 Sprout Fund

Welcome to Sprout Fund, the platform that empowers financial inclusion through micro-investments. This README file provides all the necessary information to get you started with the Sprout Fund project.

## Table of Contents
- [Project Overview](#project-overview)
- [Mission and Vision](#mission-and-vision)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
Sprout Fund is a micro-investment platform that allows users to invest small amounts of money in startups by rounding up their everyday transactions. The platform is designed to make investing accessible to everyone, regardless of their financial literacy or disposable income.

## Mission and Vision
**Mission:** Empowering Financial Inclusion Through Micro-Investments.

**Vision:** To be the leading platform in Europe that transforms everyday transactions into powerful investment opportunities, fostering financial inclusion for all.

## Features

- 🔐 **User Authentication and Onboarding:** Secure login and user registration with multi-factor authentication.
- 🏦 **Bank Account Integration:** Seamless transaction rounding and fund transfers using PSD2 connections.[FUTURE]
- 📊 **Investment Dashboard:** A user-friendly interface to track investments, view startup profiles, and monitor portfolio performance.
- 🤖 **Automated Transaction Processing:** Backend systems to automate the rounding up of transactions and investment of funds. [FUTURE]
- 📚 **Educational Resources:** Personalized financial insights and educational resources to empower users to make informed investment decisions. [FUTURE]

## Technical Stack

- **🖥️ Backend:** Django Framework
- **💻 Frontend:** HTML, CSS, JavaScript
- **💾 Database:** SQLite (development), PostgreSQL (production)
- **☁️ Hosting:** PythonAnywhere (current), Google Cloud (future)
- **🔗 Version Control:** GitHub

## Installation

Follow these steps to set up the project locally:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MauritsGraaf/Fintech-course.git
   cd Fintech-course

2. **Create and activate virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
## Usage
Accessing the platform
1. Open your web browser and navigate to http://127.0.0.1:8000.
2. Register a new user account or log in with your superuser credentials.
3. Link your bank account to start rounding up transactions.
4. Explore the investment dashboard to view and manage your investments. 📈

### Admin Panel
Access the Django admin panel at http://127.0.0.1:8000/admin to manage users, startups, and transactions. 🔧

## Contributing
We welcome contributions to Sprout Fund! To contribute:
1. Fork the repository. 🍴
2. Create a new branch: git checkout -b feature-branch.
3. Make your changes and commit them: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature-branch.
5. Submit a pull request. 🔄

## License
This project is licensed under the MIT License. 📜

## Contact
For questions or support, please contact:

Maurits Graaf - CEO, Sprout Fund
Email: maurits.graaf@hotmail.com 📧

Visit our website: Sprout Fund
https://mauritsgraaf1.pythonanywhere.com/

Thank you for using Sprout Fund! 🌟
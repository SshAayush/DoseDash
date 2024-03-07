# Pharmacy eCommerce Site

This project is a pharmacy eCommerce website built using Django and SQLite. It features a reminder system to notify users when it's time to buy certain products.

## Features

- User registration and authentication
- Product listing and search
- Shopping cart functionality
- Reminder system for product purchases
- Admin dashboard for managing products and user reminders

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- SQLite (included with Django)

### Installation

1. Clone the repository: git clone [https://github.com/yourusername/pharmacy-ecommerce.git](https://github.com/SshAayush/DoseDash.git)https://github.com/SshAayush/DoseDash.git
2. Navigate to the project directory: cd DoseDash
3. Install the environment(conda)
4. Apply migrations to set up the database: python manage.py migrate
5. Create a superuser for the admin dashboard (optional): python manage.py createsuperuser
6. Run the development server: python manage.py runserver

## Setting up Environment

You can use the requirements.txt file to recreate the environment or install the packages in another environment. To create a new environment with the packages listed in requirements.txt, you can use:

**Use the requirements.txt File**
```
conda create --name new_environment_name --file requirements.txt
```

**To install the packages in an existing environment, you can use:**
```
conda install --file requirements.txt
```

## Usage

After setting up the project, you can access the website by navigating to `http://127.0.0.1:8000/` in your web browser.

- **User Registration and Login**: Navigate to `/signup/` to register a new user or `/signin/` to log in.
- **Product Listing**: Browse products by navigating to `/shop/`.
- **Shopping Cart**: Add products to your cart and view it at `/cart/`.
- **Reminders**: Set reminders for product purchases through the user dashboard.
  
  **To start a Celery Task start beat and worker task**:
  ```
  celery -A DoseDash beat --loglevel=info
  ```
  ```
  celery -A DoseDash worker --loglevel=info
  ```

## Contact

Name: Aayush Timalsina

Email - xayush.dc@gmail.com

Project Link: https://github.com/SshAayush/DoseDash

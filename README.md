# Django E-Commerce Project

## Overview
This is a full-featured e-commerce web application built with Django. The project includes essential e-commerce functionalities such as user authentication, product management, shopping cart, wishlist, order processing, and email services.

## Features
- **User Authentication:** Register, login, logout, and profile management.
- **MySQL Database:** Stores user and product data efficiently.
- **Email Services:** Email verification, order confirmation, and password reset.
- **Password Reset Links:** Secure password reset via email.
- **Shopping Cart:** Add, remove, and update products in the cart.
- **Wishlist:** Save favorite products for future purchases.
- **Orders:** Place and track orders.
- **Common Functionalities:** Search, filters, and responsive UI.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- MySQL
- Virtual Environment

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-django.git
   cd ecommerce-django
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure MySQL database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` to access the website.
- Register or log in to explore products.
- Add products to the cart or wishlist.
- Place an order and receive an email confirmation.
- Reset password via email if needed.

## Email Configuration
In `settings.py`, configure Gmail SMTP:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.


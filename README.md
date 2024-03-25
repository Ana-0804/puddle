# Puddle E-commerce Website

Puddle is a Django-based e-commerce website for selling various products. It provides a platform for users to browse, search, and purchase items online.

## Features

- User authentication and authorization
- Product browsing and searching
- Shopping cart functionality
- Checkout process with order tracking
- Admin panel for managing products, orders, and users
- Integration with a default database (SQLite) provided by Django

## Technologies Used

- Django: A high-level Python web framework for rapid development of secure and maintainable websites.
- HTML/CSS: Frontend design and styling.
- SQLite: Default database provided by Django for development purposes.
- JavaScript: Used for client-side interactivity and form validation.

## Setup

1. Clone the repository:

git clone


2. Navigate to the project directory:

cd puddle


3. Create a virtual environment:


4. Activate the virtual environment:

- On Windows:

env\Scripts\activate


5. Install the required dependencies:

pip install -r requirements.txt


6. Run database migrations:

python manage.py migrate


7. Create a superuser account:

python manage.py createsuperuser


8. Start the development server:

python manage.py runserver


9. Access the website in your browser at `http://127.0.0.1:8000/`.

## Usage

- Visit the website and browse through the available products.
- Add items to your cart and proceed to checkout to place an order.
- Use the admin panel (`http://127.0.0.1:8000/admin/`) to manage products, orders, and user accounts.


## License

This project is licensed under the [MIT License](LICENSE).


# Stock Management Project

The Stock Management Project is a web application built using the Django framework for the backend and HTML, CSS, and JavaScript for the frontend. This application is designed to help businesses and organizations manage their stock inventory efficiently.

## Features

- **Dashboard:** An overview of stock status, including stock levels, recent transactions, and alerts.
- **Product Management:** Add, update, and delete products from the inventory.
- **Stock Tracking:** Keep track of stock quantities, restocking, and sales.
- **Transaction History:** Maintain a history of all stock-related transactions.
- **Alerts and Notifications:** Get alerts for low stock levels or other important events.
- **Responsive Design:** The frontend is built using HTML, CSS, and JavaScript to ensure a user-friendly experience across devices.

## Installation

1. Clone the repository:
```shell
   git clone https://github.com/bothrajat/Stock-Management.git
```
2. Create a virtual environment and activate it:

```shell
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required dependencies:
```shell
pip install -r requirements.txt
```
4. Set up the database:
```shell
python manage.py migrate
```
5. Run the development server:
```shell
python manage.py runserver
```
6. Access the application by navigating to http://localhost:8000 in your web browser.
## Usage
1. Open the application by navigating to http://localhost:8000 in your web browser.
2. Explore the dashboard to manage products, track stock, and view transaction history.
3. Use the provided forms and interfaces to perform stock-related actions.
4. Receive notifications or alerts for low stock levels or other important events.
## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or create a pull request on the GitHub repository.

## License
This project is unlicensed

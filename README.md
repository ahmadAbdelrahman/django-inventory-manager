# Inventory & Sales Management System

A Django web app for managing inventory, sales, and PDF invoices, designed for small businesses. 
It includes user authentication, product and customer management, and order creation with multiple products per order.

## Features
- User login/logout
- Add/edit customers and products
- Create sales orders with multiple items
- Automatically calculate totals
- Bootstrap-styled UI
- Inline formsets for multiple sales items per order

## Tech Stack
- Python 3.x
- Django 4.x
- SQLite (default)
- Bootstrap 5


project-root/
│
├── core/ # Main app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ └── core/
│
├── templates/ # Global templates
│ └── base.html
│
├── db.sqlite3
├── manage.py
└── requirements.txt # Python dependencies

## ⚙️ Getting Started

1. **Clone the repo**  
    ```bash
    git clone https://github.com/ahmadAbdelrahman/django-inventory-manager
    cd inventory-sales-system
    
2. **Create a virtual environment**
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    
3. **Install dependencies**
    pip install -r requirements.txt




## Getting Started
```bash
git clone https://github.com/ahmadAbdelrahman/django-inventory-manager
cd inventory-sales-system
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

# Django Sales Management App

This is a simple, functional Django web application for managing sales orders.  
It includes user authentication, product and customer management, and order creation with multiple products per order.

## 🚀 Features

- User login/logout
- Add/edit customers and products
- Create sales orders with multiple items
- Automatically calculate totals
- Bootstrap-styled UI
- Inline formsets for multiple sales items per order

## 📸 Screenshots

> _(Add screenshots later for a more professional presentation)_

## 🏗️ Built With

- Python 3.x
- Django 4.x
- SQLite (default)
- Bootstrap 5

## 📂 Folder Structure
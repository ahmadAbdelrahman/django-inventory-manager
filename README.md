# Django Inventory Manager

This is a simple, functional Django web application for managing sales orders.  
It includes user authentication, product and customer management, and order creation with multiple products per order.

## 🚀 Features
- User authentication
- Customer & product management
- Create and manage sales orders
- Inline item entry (using inline formsets)
- Dynamic total calculations
- Filtering & search
- User-based data visibility
- PDF order generation
- Admin panel

## 🧰 Tech Stack
- Django
- SQLite
- Bootstrap
- HTML + CSS + JS (Django Templates)

## ⚙️ Getting Started

1. **Clone the repo**  
```bash
    git clone https://github.com/yourusername/django-inventory-manager.git
    cd InventoryManager
```

2. **Create a virtual environment**
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
    pip install -r requirements.txt
```

4. **Run migrations**
```bash
    python manage.py makemigrations
    python manage.py migrate
```

5. **Create superuser (admin account)**
```bash
    python manage.py createsuperuser
```

6. **Start the development server**
```bash
    python manage.py runserver
```

7. **Access the app**
```bash
    App: http://127.0.0.1:8000/
    Admin: http://127.0.0.1:8000/admin/
```

## 📎 Demo

- Deployed link here (https://django-inventory-manager-65ag.onrender.com)

## 📄 License

MIT License — feel free to use and modify.

## 👤 Author

Ahmed Abdelrahman
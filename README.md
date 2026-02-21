# Django Admin Exploration 🚀

A hands-on project to explore Django’s built-in Admin Panel including superuser creation, model registration, admin customization, and image upload handling.

---

## 📌 About This Project

This project focuses on understanding how Django’s default admin interface works and how developers can customize it using `models.py` and `admin.py`.

It demonstrates:

- Creating a Django project and app
- Creating a superuser
- Registering models in admin
- Customizing admin display
- Uploading and displaying images using `ImageField`

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- SQLite (default database)

---

## 📂 Project Structure
core/
│
├── accounts/
│ ├── migrations/
│ ├── models.py
│ ├── admin.py
│ ├── views.py
│ └── apps.py
│── core
|   ├── wsgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── asgi.py    
├── students_img/
├── db.sqlite3
├── manage.py
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gmlincoln/django-admin-exploration-b2
cd core
```

### 2️⃣ Create Virtual Environment (Recommended)

#### Mac/Linux:
```bash
python -m venv venv
source venv/bin/activate
```
#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
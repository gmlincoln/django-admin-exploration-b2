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
```bash
core/
│
├── accounts/
│ ├── migrations/
│ ├── models.py
│ ├── admin.py
│ ├── views.py
│ └── apps.py
│── core
│  ├── wsgi.py
│  ├── settings.py
│  ├── urls.py
│  ├── views.py
│  └── asgi.py    
├── students_img/
├── db.sqlite3
├── manage.py
└── README.md
```



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

### 3️⃣ Install Dependencies

```bash
pip install django

```
If you are using image fields, also install:
```bash
pip install pillow
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser

```

##### Enter:
- Username  
- Email  
- Password
- Confirm Password  

### 6️⃣ Run the Development Server

```bash 

python manage.py runserver

```

python manage.py runserver

Open your browser and visit:

```bash
http://127.0.0.1:8000/admin/
```
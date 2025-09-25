# Task Pilot

Welcome to **Task Pilot** 🎉 — a simple yet powerful task management tool built with **Flask** and **SQLite**.  

Stay organized and never miss a task again! Task Pilot allows you to efficiently manage your daily tasks with ease.

---

## 📌 Features
- User authentication (register & login)
- Create, edit, and delete todos
- Priortize your todos
- Simple and clean UI with custom CSS/JS
- SQLite database (can be switched to MySQL/Postgres)

---

## 📂 Project 

```bash
todos/
│── app/
│ ├── routes/ # Flask blueprints (auth & tweets)
│ ├── static/ # JS & CSS files
│ ├── templates/ # HTML templates
│ ├── models.py # Database models
│ └── init.py # App factory
│── instance/ # Local DB (ignored by git)
│── run.py # Entry point

```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ayushWeb07/Task-Pilot.git
cd Task-Pilot
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Rum the app
```bash
python run.py
```

---

## 🛠️ Tech Stack

- **Backend:** Flask, SQLAlchemy
    
- **Frontend:** HTML, CSS, JS (Jinja2 templates)
    
- **Database:** SQLite (default)
    

---

## 📸 Screenshots

![Login](/assets/login.png)
![Register](/assets/register.png)
![Home](/assets/home.png)
![Todos list](/assets/todos-list.png)
![About](/assets/about.png)



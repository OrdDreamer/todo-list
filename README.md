# ✅ Todo List - Task Management Application

## 📘 Project Description

**Todo List** is a simple and efficient web application for managing your daily tasks. The system allows you to create tasks, organize them with tags, set deadlines, and track their completion status.

Key features:
- create and manage tasks
- organize tasks with tags
- set optional deadlines
- mark tasks as completed or undone
- view tasks sorted by status and creation date

---

## ✨ Features

### Task Management
- **CRUD operations**: create, view, edit, and delete tasks
- **Task content**: detailed description of what needs to be done
- **Deadlines**: optional deadline datetime for tasks
- **Completion status**: mark tasks as completed or undone with a single click
- **Task ordering**: tasks are automatically sorted by status (not done first) and creation date (newest first)
- **Tags**: assign multiple tags to tasks for better organization

### Tag Management
- **CRUD operations**: create, view, edit, and delete tags
- **Tag assignment**: assign multiple tags to tasks
- **Tag list**: view all available tags in a table format

---

## 🛠️ Technologies

- **Python 3.8+**
- **Django 6.0**
- **SQLite**
- **Bootstrap 5**
- **Django Crispy Forms**

---

## 📋 Installation

### Requirements

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the repository

```bash
git clone <repository-url>
cd todo-list
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply migrations

```bash
python manage.py migrate
```

### Step 5: Create a superuser (optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

---

## 🚀 Running the Project

After completing all installation steps, start the development server:

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

---

## 📁 Project Structure

```
todo-list/
├── core/                      # Main Django project
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL routes
│   ├── asgi.py
│   └── wsgi.py
├── tasks/                     # Tasks application
│   ├── __init__.py
│   ├── models.py              # Task and Tag models
│   ├── views.py               # Views
│   ├── forms.py               # Forms
│   ├── urls.py                # URL routes
│   ├── admin.py               # Admin panel settings
│   └── templates/             # Task templates
│       └── tasks/
│           ├── task_list.html
│           ├── task_form.html
│           ├── task_confirm_delete.html
│           ├── tag_list.html
│           ├── tag_form.html
│           └── tag_confirm_delete.html
├── templates/                 # Base templates
│   ├── base.html              # Base template
│   └── includes/
│       ├── sidebar.html       # Sidebar navigation
│       └── pagination.html    # Pagination component
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation
```

---

## 🗄️ Data Models

### Tag
- `name` — tag name (unique)
- Relationship: Tag ↔ Task (ManyToMany)

### Task
- `content` — task description (TextField)
- `created_at` — datetime when task was created (auto-generated)
- `deadline` — optional deadline datetime (nullable)
- `is_done` — completion status (Boolean, default: False)
- `tags` — related tags (ManyToMany to Tag)
- Relationships:
  - Task ↔ Tag (ManyToMany)

---

## 🔗 Main URL Routes

- `/` — home page (task list)
- `/task/create/` — create new task
- `/task/<id>/update/` — edit task
- `/task/<id>/delete/` — delete task
- `/task/<id>/toggle/` — toggle task completion status
- `/tags/` — tag list
- `/tag/create/` — create new tag
- `/tag/<id>/update/` — edit tag
- `/tag/<id>/delete/` — delete tag
- `/admin/` — Django admin panel

---

## 📝 Additional Notes

- Tasks are automatically ordered by completion status (not done first) and creation date (newest first)
- Pagination is used for the task list (20 items per page)
- Forms are styled using Bootstrap 5 via Django Crispy Forms
- The sidebar is present on all pages for easy navigation
- Task completion status can be toggled with a single click

---

## 📄 License

This is an educational project created for educational purposes.

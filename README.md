# Autoria 🚗

A car community website built with Django. Users can register, log in, read posts about cars (reviews, cars for sale, questions, maintenance), comment on them, and publish their own posts with photos.

The project started from a "Simple Blog" assignment and was extended into a full car-themed community site.

---

## Features

### Core requirements (from the assignment)
- User **registration**, **login** and **logout**
- **Home page** listing posts
- **Post page** with title, body, all comments, and a text area for a new comment
- Logged-in users can **write comments** and **add new posts**
- One post has many comments (one-to-many relationship)

### Extra features
- **Post categories:** Review, For Sale, Question, Maintenance
- **Car fields:** brand, model year, price, and a photo
- **Edit and delete** your own posts (other users cannot)
- **Image upload** with validation (images only, max 3 MB)
- **Pagination** (6 posts per page)
- **Live search** on the post cards
- **Hero video** on the home page, with a pause/play button
- **Dark / Light theme** toggle, saved in the browser
- **English / Arabic** language toggle (with RTL support)
- Dropdown menu, responsive layout, and a full footer
- Success messages that hide automatically
- Confirmation dialog before deleting

---

## Tech Stack

| Layer | Technology |
|---|---|
| Back-end | Python, Django 6.1 |
| Database | PostgreSQL (SQLite works too, see below) |
| Front-end | HTML (Django templates), CSS, vanilla JavaScript |
| Images | Pillow |
| Fonts | Inter, Playfair Display, Cairo (Google Fonts) |

---

## Project Structure

```
blog_project/
├── manage.py
├── requirements.txt
├── blog_project/            # project settings
│   ├── settings.py
│   └── urls.py
└── blog/                    # the main app
    ├── models.py            # Post, Comment, CarModel
    ├── views.py             # page logic
    ├── forms.py             # RegisterForm, PostForm, CommentForm
    ├── urls.py              # app routes
    ├── admin.py
    ├── templates/blog/      # HTML pages
    │   ├── base.html
    │   ├── home.html
    │   ├── post_detail.html
    │   ├── post_form.html
    │   ├── register.html
    │   ├── login.html
    │   ├── _post_card.html
    │   ├── _pagination.html
    │   └── _form_fields.html
    └── static/blog/
        ├── css/style.css
        ├── js/main.js
        └── video/mercedes.mp4
```

Files that start with `_` are small reusable template pieces included in other pages.

---

## Database Design

```
User      (Django built-in)
Post      (title, brand, model_year, price, image, category, body, author -> User, created_at)
Comment   (post -> Post, author -> User, content, created_at)
CarModel  (car models shown on the Models page)
```

**Relationships**
- A user has many posts.
- A post has many comments.
- A user has many comments.

Passwords are hashed automatically by Django.

---

## Pages and Routes

| Page | URL name | Access |
|---|---|---|
| Home | `home` | Everyone |
| Models | `car_models` | Everyone |
| Buy | `buy` | Everyone |
| Services (maintenance) | `services` | Everyone |
| Post details + comments | `post_detail` | Everyone (commenting needs login) |
| New post | `post_create` | Logged-in users |
| Edit post | `post_update` | Post owner only |
| Delete post | `post_delete` | Post owner only |
| Register | `register` | Everyone |
| Login | `login` | Everyone |
| Logout | `logout` | Logged-in users |

---

## Getting Started

### 1. Requirements
- Python 3.12 or newer
- PostgreSQL (optional, only if you use it as the database)

### 2. Clone and create a virtual environment

```powershell
git clone <your-repo-url>
cd blog_project

python -m venv venv
venv\Scripts\Activate.ps1
```

On macOS / Linux: `source venv/bin/activate`

If PowerShell blocks the script, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

Or manually:

```powershell
python -m pip install django pillow "psycopg[binary]"
```

### 4. Configure the database

**Option A: PostgreSQL** (used in this project)

Create a database named `autoria` (in pgAdmin, or with `CREATE DATABASE autoria;`), then set your credentials in `blog_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'autoria',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**Option B: SQLite** (no setup needed)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 5. Add the hero video

The video file is not included in the repository because of its size. Download a short Mercedes clip (for example from Pexels or Pixabay), name it `mercedes.mp4`, and place it here:

```
blog/static/blog/video/mercedes.mp4
```

Without it the site still works, the hero area just has a black background.

### 6. Create the tables and an admin account

```powershell
python manage.py migrate
python manage.py createsuperuser
```

### 7. Run the server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the site and http://127.0.0.1:8000/admin for the admin panel.

---

## How to Use

1. Open the site and browse the posts.
2. Click the **three dots** menu, then **Sign up** to create an account.
3. Use **New post** to publish a post (choose a category and upload a photo).
4. Open any post and write a comment at the bottom.
5. Edit or delete your own posts from the post page.
6. Use the theme button to switch dark/light, and the language button to switch English/Arabic.

---

## Security Notes

- Passwords are hashed by Django's authentication system.
- All forms use CSRF protection.
- Template output is escaped automatically (protects against XSS).
- Django ORM prevents SQL injection.
- Posting and commenting require login, and only the owner can edit or delete a post.
- Uploaded files are validated as images and limited to 3 MB.

Before deploying to a real server:
- Set `DEBUG = False` and configure `ALLOWED_HOSTS`.
- Move `SECRET_KEY` and the database password to environment variables.
- Serve

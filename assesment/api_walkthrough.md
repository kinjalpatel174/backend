# EduTracker API Walkthrough

Welcome to the **EduTracker Solutions** REST API. This API allows you to manage students and courses seamlessly.

## 🚀 Getting Started

### 1. Project Setup
The project is already initialized with:
- **Django 6.x** & **DRF 3.x**
- **SQLite** database
- **Token Authentication** support

### 2. Running the Server
```bash
python manage.py runserver
```

### 3. API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/courses/` | GET | List all courses |
| `/api/courses/` | POST | Create a new course |
| `/api/students/` | GET | List all students (includes course details) |
| `/api/students/` | POST | Register a new student |
| `/api-token-auth/`| POST | Obtain Auth Token (requires credentials) |

### 4. Example Requests

#### Create a Student (POST)
**URL:** `/api/students/`
**Body (JSON):**
```json
{
    "first_name": "Alice",
    "last_name": "Johnson",
    "email": "alice.j@example.com",
    "dob": "1998-04-12",
    "courses": [1, 2]
}
```

#### Search for a Course
**URL:** `/api/courses/?search=Python`

## 🛡️ Authentication
This API uses **Token Authentication**.
1. Send a POST request to `/api-token-auth/` with `username` and `password`.
2. Include the token in your headers:
   `Authorization: Token your_generated_token_here`

## 📁 Key Files
- `core/models.py`: Database structure.
- `core/serializers.py`: Data transformation logic.
- `core/views.py`: API logic (ViewSets).
- `seed_data.py`: Run `python seed_data.py` to populate data.

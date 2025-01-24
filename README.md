Here’s your updated **`README.md`** file written in the requested format:

---

```markdown
# flouci_auth

A Django-based API authentication system with support for JWT, API keys, and session-based authentication.

---

## Features

### Core Functionality
- **JWT Authentication**:
  - Secure token-based login and post-fetching.
- **API Key Authentication**:
  - Access to specific endpoints using API keys.
- **Session Authentication**:
  - Post creation with CSRF token validation.
- **CRUD for Posts**:
  - Create, view, and list posts.

---

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **SQLite** (or another supported Django database backend)

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/nadiatrabelsii/flouci_auth.git
cd flouci_auth
```

---

### Step 2: Set Up the Python Environment
1. Install `virtualenv` if not already installed:
   ```bash
   pip install virtualenv
   ```
2. Create and activate a virtual environment:
   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

---

### Step 3: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

---

### Step 4: Apply Migrations
1. Apply Django database migrations:
   ```bash
   python manage.py migrate
   ```

---

### Step 5: Create a Superuser
Run the following command to create an admin user:
```bash
python manage.py createsuperuser
```

---

### Step 6: Run the Development Server
Start the server:
```bash
python manage.py runserver
```

---

## API Endpoints

### Authentication
1. **Obtain JWT Token**:
   - `POST /api/token/`
   - Payload: `{"username": "your_username", "password": "your_password"}`

2. **Refresh JWT Token**:
   - `POST /api/token/refresh/`

3. **Custom Login with CSRF**:
   - `POST /login/`
   - Payload: `{"username": "your_username", "password": "your_password"}`

---

### Posts
1. **List All Posts**:
   - `GET /api/posts/`
   - **JWT Authentication** required.

2. **View Post by ID**:
   - `GET /api/posts/<id>/`
   - **API Key Authentication** required.
   - Add header: `Authorization: Api-Key <your-api-key>`

3. **Create a Post**:
   - `POST /api/posts/create/`
   - **Session Authentication** required.
   - Add headers: `X-CSRFToken` and `Cookie`.

---

## Running Tests
Run the test suite with:
```bash
python manage.py test
```

---

## Contributing

Follow these steps to contribute to the project:

1. **Fork the Repository**:
   ```bash
   git fork https://github.com/nadiatrabelsii/flouci_auth.git
   ```
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
4. **Push Your Branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Submit a Pull Request**:
   - Go to the repository on GitHub.
   - Click **Pull Requests** > **New Pull Request**.
   - Submit your changes for review.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Project Structure

flouci_auth/
├── api/                         # Core application for API
│   ├── migrations/              # Database migrations for the API app
│   ├── __init__.py              # Python package initialization
│   ├── admin.py                 # Admin configuration for API models
│   ├── apps.py                  # App configuration for API
│   ├── models.py                # Database models for API (e.g., Post, UserAPIKey)
│   ├── serializers.py           # Serializers for DRF (e.g., PostSerializer)
│   ├── tests.py                 # Unit tests for API views, models, and serializers
│   ├── urls.py                  # URL patterns for API endpoints
│   └── views.py                 # Views for handling API requests
├── auth_flouci/                 # Main project configuration directory
│   ├── __init__.py              # Python package initialization
│   ├── asgi.py                  # ASGI configuration for asynchronous support
│   ├── settings.py              # Project settings (database, middleware, etc.)
│   ├── urls.py                  # Root URL configuration
│   └── wsgi.py                  # WSGI configuration for deployment
├── venv/                        # Python virtual environment (dependencies installed here)
├── staticfiles/                 # Collected static files for deployment (optional)
├── db.sqlite3                   # SQLite database file
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies for the project
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore file
├── Capture1.JPG                 # pictures of my testing in Postman
├── Capture2.JPG
├── Capture3.JPG
└── Capture4.JPG

## Contact

For questions or support, contact:

- **Email**: Trabelsi.Nadia@esprit.tn
```

---

### Save and Commit to GitHub
1. Save this file as `README.md` in your project directory.
2. Add and commit it to GitHub:
   ```bash
   git add README.md
   git commit -m "Add README.md"
   git push origin main
   ```

Let me know if you'd like to add or modify anything further! 🚀
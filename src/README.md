# Mergington High School Activities API

A FastAPI application that allows students to view and sign up for extracurricular activities, now backed by persistent SQLite storage.

## Features

- View all available extracurricular activities
- Sign up for activities
- Unregister students from activities
- Persist data across server restarts
- Run schema migrations and local seed data

## Getting Started

1. Install the dependencies:

   ```
   pip install -r ../requirements.txt
   ```

2. Run migrations (includes initial seed data):

   ```
   python manage_db.py migrate
   ```

3. Run the application:

   ```
   uvicorn app:app --reload
   ```

4. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## Database Commands

Run these from the `src` directory:

```
python manage_db.py migrate   # Apply unapplied migrations
python manage_db.py reset     # Delete local SQLite database
python manage_db.py reseed    # Reset + apply migrations and seed data
```

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister from an activity                                         |

## Data Model

The application uses SQLite with migration files under `src/migrations`.

Core tables:

- `students`
- `activities`
- `activity_registrations`
- `users`
- `clubs`
- `club_memberships`
- `events`
- `event_registrations`

The current UI endpoints primarily use `activities`, `students`, and `activity_registrations`, while the other tables provide the foundation for future role-based and event-management features.

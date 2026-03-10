"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

from database import (
    ensure_student,
    fetch_activities_with_participants,
    get_activity_by_name,
    get_connection,
    run_migrations,
)

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

@app.on_event("startup")
def startup() -> None:
    run_migrations()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    with get_connection() as conn:
        return fetch_activities_with_participants(conn)


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    with get_connection() as conn:
        activity = get_activity_by_name(conn, activity_name)
        if activity is None:
            raise HTTPException(status_code=404, detail="Activity not found")

        student_id = ensure_student(conn, email)
        participant_count = conn.execute(
            "SELECT COUNT(*) AS count FROM activity_registrations WHERE activity_id = ?",
            (activity["id"],),
        ).fetchone()["count"]
        if participant_count >= activity["max_participants"]:
            raise HTTPException(status_code=400, detail="Activity is full")

        already_registered = conn.execute(
            """
            SELECT 1
            FROM activity_registrations
            WHERE activity_id = ? AND student_id = ?
            """,
            (activity["id"], student_id),
        ).fetchone()
        if already_registered:
            raise HTTPException(status_code=400, detail="Student is already signed up")

        conn.execute(
            "INSERT INTO activity_registrations (activity_id, student_id) VALUES (?, ?)",
            (activity["id"], student_id),
        )

    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    with get_connection() as conn:
        activity = get_activity_by_name(conn, activity_name)
        if activity is None:
            raise HTTPException(status_code=404, detail="Activity not found")

        student = conn.execute(
            "SELECT id FROM students WHERE email = ?",
            (email,),
        ).fetchone()
        if student is None:
            raise HTTPException(
                status_code=400,
                detail="Student is not signed up for this activity"
            )

        result = conn.execute(
            "DELETE FROM activity_registrations WHERE activity_id = ? AND student_id = ?",
            (activity["id"], student["id"]),
        )
        if result.rowcount == 0:
            raise HTTPException(
                status_code=400,
                detail="Student is not signed up for this activity"
            )

    return {"message": f"Unregistered {email} from {activity_name}"}

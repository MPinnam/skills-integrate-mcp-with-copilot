"""Database helpers for migrations, seeding, and common queries."""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from typing import Iterator
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "school.db"
MIGRATIONS_DIR = BASE_DIR / "migrations"


def _ensure_foreign_keys(conn: sqlite3.Connection) -> None:
    conn.execute("PRAGMA foreign_keys = ON")


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _ensure_foreign_keys(conn)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def run_migrations() -> None:
    migration_files = sorted(MIGRATIONS_DIR.glob("*.sql"))
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version TEXT PRIMARY KEY,
                applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        applied_versions = {
            row["version"]
            for row in conn.execute("SELECT version FROM schema_migrations")
        }

        for migration_path in migration_files:
            version = migration_path.name
            if version in applied_versions:
                continue

            conn.executescript(migration_path.read_text(encoding="utf-8"))
            conn.execute(
                "INSERT INTO schema_migrations (version) VALUES (?)",
                (version,),
            )


def ensure_student(conn: sqlite3.Connection, email: str) -> int:
    existing = conn.execute(
        "SELECT id FROM students WHERE email = ?",
        (email,),
    ).fetchone()
    if existing:
        return int(existing["id"])

    default_name = email.split("@", maxsplit=1)[0].replace(".", " ").title()
    cursor = conn.execute(
        "INSERT INTO students (email, name) VALUES (?, ?)",
        (email, default_name),
    )
    return int(cursor.lastrowid)


def get_activity_by_name(conn: sqlite3.Connection, activity_name: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT id, name, description, schedule, max_participants FROM activities WHERE name = ?",
        (activity_name,),
    ).fetchone()


def fetch_activities_with_participants(conn: sqlite3.Connection) -> dict[str, dict[str, object]]:
    activities = conn.execute(
        "SELECT id, name, description, schedule, max_participants FROM activities ORDER BY name"
    ).fetchall()

    result: dict[str, dict[str, object]] = {}
    for activity in activities:
        participants = conn.execute(
            """
            SELECT s.email
            FROM activity_registrations ar
            JOIN students s ON s.id = ar.student_id
            WHERE ar.activity_id = ?
            ORDER BY ar.id
            """,
            (activity["id"],),
        ).fetchall()

        result[str(activity["name"])] = {
            "description": activity["description"],
            "schedule": activity["schedule"],
            "max_participants": activity["max_participants"],
            "participants": [row["email"] for row in participants],
        }

    return result

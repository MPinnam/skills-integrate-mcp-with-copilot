"""Simple database management utility for migrations and local resets."""

from __future__ import annotations

import argparse
from pathlib import Path

from database import DB_PATH, run_migrations


def reset_database() -> None:
    if Path(DB_PATH).exists():
        Path(DB_PATH).unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage local SQLite database")
    parser.add_argument(
        "command",
        choices=["migrate", "reset", "reseed"],
        help="Database command to execute",
    )
    args = parser.parse_args()

    if args.command == "reset":
        reset_database()
        print("Database reset complete.")
        return

    if args.command == "reseed":
        reset_database()
        run_migrations()
        print("Database reseeded from migrations.")
        return

    run_migrations()
    print("Migrations complete.")


if __name__ == "__main__":
    main()

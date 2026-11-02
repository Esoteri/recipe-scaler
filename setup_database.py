import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "data" / "recipes.db"

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DATABASE_PATH)

connection.close()

print("Recipe database created successfully!")

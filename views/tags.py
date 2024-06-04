import sqlite3
import json
from datetime import datetime
import logging

def list_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    db_cursor.execute(
            """
        SELECT *
            FROM Tags
        """,
            (),
        )
    
    query_results = db_cursor.fetchall()
    tags=[]
    for row in query_results:
        tags.append(dict(row))
    serialized_posts = json.dumps(tags)
    return serialized_posts

def insert_tag(tag_data):
    try:
        with sqlite3.connect("./db.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                INSERT INTO Tags (label)
                    VALUES (
                       ?
                        )
                """,
                (tag_data['label'],)
            )

            if db_cursor.rowcount > 0:
                return True
            else:
                return False
    except Exception as e:
        logging.error(f"Failed to insert tag: {e}")
        return None

def update_tag(pk, tag_data):
    try:
        with sqlite3.connect("./db.sqlite3") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(
                """
                UPDATE Tags
                SET label = ?
                WHERE id = ?
                """,
                (tag_data['label'], pk)
            )
            if db_cursor.rowcount > 0:
                return True
            else:
                return False

    except Exception as e:
        logging.error(f"Failed to update tag: {e}")
        return None

def delete_tag(pk):
    try:
        with sqlite3.connect("./db.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Write the SQL query to get the information you want
            db_cursor.execute("""
            DELETE FROM Tags WHERE id = ?
            """, (pk,)
            )
            if db_cursor.rowcount > 0:
                return True
            else:
                return False

    except Exception as e:
        logging.error(f"Failed to update tag: {e}")
        return None
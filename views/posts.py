import sqlite3
import json
from datetime import datetime


def retrieve_post(url):

    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    if url["query_params"] == {}:

        db_cursor.execute(
            """
        SELECT *
            FROM Posts
            WHERE id =?;
        """,
            (url["pk"],),
        )
        query_results = db_cursor.fetchone()

        dictionary_version_of_object = dict(query_results)
        serialized_ship = json.dumps(dictionary_version_of_object)

    elif "_expand" in url["query_params"]:
        db_cursor.execute(
            """
       SELECT Posts.*, Users.id AS user_id, Users.username, Users.email
            FROM Posts
            JOIN Users ON Posts.user_Id = Users.id
            WHERE Posts.id =?
        """,
            (url["pk"],),
        )

        query_results = db_cursor.fetchone()

        dictionary_version_of_object = dict(query_results)
        serialized_ship = json.dumps(dictionary_version_of_object)

    return serialized_ship


def list_posts(url):

    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    if "_expand" in url["query_params"]:

        db_cursor.execute(
            """
            SELECT Posts.* , Users.id AS User_id, Users.username, Users.email, Categories.*
            FROM Posts
            JOIN Users ON Posts.user_Id = Users.id  
            JOIN Categories ON Posts.category_id = Categories.id            
          
        """,
        )

        query_results = db_cursor.fetchall()

        posts = []
        for row in query_results:
            posts.append(dict(row))

        serialized_posts = json.dumps(posts)

        return serialized_posts


def create_post(post_data):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
            INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved) VALUES (?,?,?,?,?,?,1)
        """,
            (
                post_data["user_id"],
                post_data["category_id"],
                post_data["title"],
                post_data["publication_date"],
                post_data["image_url"],
                post_data["content"],
                post_data["approved"],
                datetime.now(),
            ),
        )
        conn.commit()
        return True
    return False

import sqlite3
import json


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

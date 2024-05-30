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

    return serialized_ship

def list_posts(url):

    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    if "_expand" in url["query_params"]:

        db_cursor.execute("""
            SELECT Posts.* , Users.id AS User_id, Users.username, Users.email, Categories.*
            FROM Posts
            JOIN Users ON Posts.user_Id = Users.id  
            JOIN Categories ON Posts.category_id = Categories.id            
          
        """, )

        query_results = db_cursor.fetchall()

        posts=[]
        for row in query_results:
            posts.append(dict(row))

        serialized_posts = json.dumps(posts)
        
        return serialized_posts
        


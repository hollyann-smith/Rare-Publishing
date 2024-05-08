import sqlite3
import json
from models import Post

POSTS = []

def get_all_posts():
  with sqlite3.connect("./db.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""
    SELECT
        p.id,
        p.category_id,
        p.user_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved
    From post p
    """)
    posts = []
    dataset = db_cursor.fetchall()
    for row in dataset:
        post = Post(row['id'], row["category_id"], row['user_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
        
        posts.append(post.__dict__)
    
    return posts

def get_single_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.category_id,
            p.user_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
    From post p
        WHERE p.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        post = Post(data['id'], data["categoty_id"], data['user_id'], data['title'], data['publication_date'], data['image_url'], data['content'], data['approved'])

        return post.__dict__

def create_post(post):
    max_id = POSTS[-1]["id"]
    new_id = max_id + 1
    post["id"] = new_id
    POSTS.append(post)
    return post

def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM comment
        WHERE post_id = ?
        """, (id, ))

        # Delete the post itself
        db_cursor.execute("""
        DELETE FROM post
        WHERE id = ?
        """, (id, ))

        
def update_post(id, new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Post
            SET
                category_id = ?,
                title = ?,
                publication_date = ?
                image_url = ?
                content = ?
                approved = ?
        WHERE id = ?
        """, (new_post['category_id'],
              new_post['title'], new_post['image_url'], new_post['publication_date'], new_post['content'], new_post['approved'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

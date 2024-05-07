import sqlite3
import json
from models import Post
POSTS = [
  {
    "id": 1,
    "user_id": 1,
    "title": "This old pho",
    "pulication_date": "Jan 1, 2018",
    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1i9-AGJRH34Q-KjbZwwIfe87A7-M3kYv8ag&s",
    "content": "5 out of 5, 10 out 10, amazing, incredible, I'll never pho anywhere else again",
    "approved": True
  },
  {
    "id": 1,
    "user_id": 2,
    "title": "Om nom nom nom",
    "pulication_date": "Jan 6, 2023",
    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6vJ9zo13iMqDYFXdo5-h233gC5RExuPbDXA&s",
    "content": "I don't know what it tasted like, I inhaled that entire meal",
    "approved": True
  }
]

def get_all_posts():
  with sqlite3.connect("./dbsqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""
    SELECT
        p.id,
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
        post = Post(row['id'], row['user_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
        
        posts.append(post.__dict__)
    
    return posts

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
        DELETE FROM post
        WHERE id = ?
        """, (id, ))

        
def update_post(id, new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Post
            SET
                name = ?,
                user_id = ?,
                title = ?,
                publication_date = ?
                image_url = ?
                content = ?
                approved = ?
        WHERE id = ?
        """, (new_post['user_id'], new_post['user_id'],
              new_post['title'], new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

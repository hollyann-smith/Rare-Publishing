import sqlite3
from models import Comment

def get_comments_by_post(post_id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.post_id,
            c.author_id,
            c.content
        from Comments c
        WHERE c.post_id = ?
        """, ( post_id, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
            comments.append(comment.__dict__)

  return comments
  
def create_comment(new_comment):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    INSERT INTO Comments
        ( post_id, content, author_id )
    VALUES
        ( ?, ?, ?, ?, ?);
    """, (new_comment['post_id'], new_comment['content'],
          new_comment['author_id'], ))

    id = db_cursor.lastrowid

    new_comment['id'] = id

  return new_comment

def update_comment(id, new_comment):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    db_cursor = conn.cursor()

    db_cursor.execute("""
    UPDATE Comments
        SET
            post_id = ?,
            content = ?,
            author_id = ?
    WHERE id = ?
    """, (new_comment['post_id'], new_comment['content'],
          new_comment['author_id'], id, ))

    rows_affected = db_cursor.rowcount

  if rows_affected == 0:
      return False
  else:
      return True

def delete_comment(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))

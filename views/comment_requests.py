import sqlite3
from models import Comment

def get_comments_by_post(post_id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT
        *
    FROM Comments c
    WHERE c.post_id = ?
    """, ( post_id, ))

    data = db_cursor.fetchone()

    comment = Comment(data['id'], data['post_id'], data['content'],
                        data['author_id'])

    return comment.__dict__
  
def create_comment(new_comment):
  with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
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
    UPDATE Animal
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
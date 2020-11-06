from uuid import uuid4
from src.database import Database
import uuid
import datetime

class Post:

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), post_id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    def save_to_mongo(self):
        Database.insert(collection="posts",
                        data=self.json())

    def json(self):
        return {
            "post_id": self.post_id,
            "blog_id": self.blog_id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "date": self.date,
        }

    @staticmethod
    def from_mongo(post_id):
        return Database.find_one(collection="posts", query={"post_id": post_id})

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection="posts", query={"blog_id": blog_id})]


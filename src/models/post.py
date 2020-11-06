from uuid import uuid4
from database import Database
import uuid
import datetime

class Post:

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection="posts",
                        data=self.json())

    def json(self):
        return {
            "id": self.id,
            "blog_id": self.blog_id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "date": self.date,
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection="posts", query={"id": id})

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection="posts", query={"blog_id": blog_id})]


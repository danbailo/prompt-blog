class Post:

    def __init__(self, blog_id, title, content, author, date, id_post):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id_post = id_post

    def save_to_mongo(self):
        Database.insert(collection="posts",
                        data=self.json())

    def json(self):
        return {
            "id_post": self.id_post,
            "blog_id": self.blog_id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "date": self.date,
        }
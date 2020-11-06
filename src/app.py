from models.post import Post
from database import Database

Database.initialize()

# post = Post(
    # blog_id="123",
    # title="great title",
    # content="great contentnteintient",
    # author="daniel bailo"
    # )

# post.save_to_mongo()

posts = Post.from_blog("123")

for post in posts:
    print(post)
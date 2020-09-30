from database import Database
# from models.post import Post
from models.blog import Blog


Database.initialize()
### add post
# post = Post(blog_id = "124", title = "first post", content = "something", author = "Lisi")
# post.save_to_mongo()

##
# post = Post.from_mongo("5f726b927739462dcaf87ec5")
# print(post)

# students = [student['mark'] for student in collection.find({})]
# print(students)

blog = Blog(author = "Lisi", title = "sample", description = "sample description")

blog.new_post()
blog.save_to_mongo()

from_database = Blog.get_from_mongo(blog.id)

print(from_database.id)


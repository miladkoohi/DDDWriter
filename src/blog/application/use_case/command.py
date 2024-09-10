# File: src/blog/application/use_case/command.py

from blog.domain.entity import BlogPost
from blog.domain.exception import BlogPostValidationError

class CreateBlogPostCommand:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author
        
    def execute(self) -> BlogPost:
        if len(self.title) < 5:
            raise BlogPostValidationError("Title must be at least 5 characters long.")
        # Assume we create and return a BlogPost instance here
        return BlogPost(title=self.title, content=self.content, author=self.author, created_at="now", updated_at="now")

from blog.domain.entity import BlogPost
from blog.domain.exception import BlogPostNotFoundException, BlogPostValidationError
from blog.infrastructure.database.repository.rdb import BlogPostRepository
from blog.application.use_case.query import GetBlogPostQuery
from blog.application.use_case.command import CreateBlogPostCommand


blog_repo = BlogPostRepository()


blog_query = GetBlogPostQuery(blog_repo)
blog_command = CreateBlogPostCommand(blog_repo)


class BlogCommand:
    def __init__(self, blog_repo):
        self.blog_repo = blog_repo

    def create_blog_post(self, title, content, author):
        # اعتبارسنجی داده‌ها قبل از ایجاد پست
        if len(title) < 5:
            raise BlogPostValidationError("Title must be at least 5 characters long.")
        new_post = BlogPost(title=title, content=content, author=author)
        return self.blog_repo.save(new_post)

    def get_blog_post(self, post_id):
        try:
            return self.blog_repo.get(post_id)
        except BlogPostNotFoundException as e:
            raise BlogPostNotFoundException(f"No blog post found with ID: {post_id}")


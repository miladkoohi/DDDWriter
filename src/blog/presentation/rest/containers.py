from blog.application.use_case.command import BlogCommand
from blog.application.use_case.query import BlogQuery
from blog.infrastructure.database.repository.rdb import BlogRDBRepository

# ایجاد نمونه‌ی repository برای بلاگ
blog_repo: BlogRDBRepository = BlogRDBRepository()

# ایجاد نمونه‌های Query و Command
blog_query: BlogQuery = BlogQuery(blog_repo=blog_repo)
blog_command: BlogCommand = BlogCommand(blog_repo=blog_repo)

from blog.application.use_case.command import BlogCommand
from blog.application.use_case.query import BlogQuery
from blog.infrastructure.database.repository.rdb import BlogRDBRepository


blog_repo: BlogRDBRepository = BlogRDBRepository()


blog_query: BlogQuery = BlogQuery(blog_repo=blog_repo)
blog_command: BlogCommand = BlogCommand(blog_repo=blog_repo)

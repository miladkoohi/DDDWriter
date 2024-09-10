from blog.domain.entity import BlogPost

class GetBlogPostQuery:
    def __init__(self, post_id: int):
        self.post_id = post_id

    def execute(self) -> BlogPost:
        # Assume we fetch and return a BlogPost instance by ID here
        # This would typically involve calling a repository
        pass

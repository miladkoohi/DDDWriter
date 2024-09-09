class BlogPostNotFoundException(Exception):
    """Exception raised when a blog post is not found."""
    pass

class BlogPostValidationError(Exception):
    """Exception raised for errors in the input data during blog post operations."""
    pass

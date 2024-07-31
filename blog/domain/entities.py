from uuid import uuid4

class Article:
    def __init__(self, title: str, content: str):
        self.id = uuid4()
        self.title = title
        self.content = content
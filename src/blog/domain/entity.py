import uuid
from dataclasses import dataclass
from typing import Optional

@dataclass(kw_only=True)
class BlogPost:
    id: Optional[uuid.UUID] = None
    title: str
    content: str
    author: str
    created_at: str
    updated_at: str

    def __eq__(self, other):
        if isinstance(other, BlogPost):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

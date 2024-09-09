from dataclasses import dataclass

@dataclass(frozen=True)
class BlogTitle:
    value: str

    def __post_init__(self):
        if len(self.value) < 5:
            raise ValueError("Title must be at least 5 characters long.")

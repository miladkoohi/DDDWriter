from typing import List, TypeVar

from django.db.models import Model
from blog.domain.entity import BlogPost
from blog.infrastructure.database.models import BlogPostModel
DjangoModelType = TypeVar("DjangoModelType", bound=Model)

class BlogPostMapper:
    def to_entity(self, instance: BlogPostModel) -> BlogPost:
        return BlogPost(
            id=instance.id,
            title=instance.title,
            content=instance.content,
            author=instance.author,
            created_at=instance.created_at,
            updated_at=instance.updated_at
        )

    def to_instance(self, entity: BlogPost) -> BlogPostModel:
        return BlogPostModel(
            id=entity.id,
            title=entity.title,
            content=entity.content,
            author=entity.author,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    def to_entity_list(self, instances: List[BlogPostModel]) -> List[BlogPost]:
        return [self.to_entity(instance=i) for i in instances]

    def to_instance_list(self, entities: List[BlogPost]) -> List[BlogPostModel]:
        return [self.to_instance(entity=e) for e in entities]

from blog.domain.entity import BlogPost
from blog.infrastructure.database.models import BlogPostModel
from blog.infrastructure.database.repository.mapper import BlogPostMapper

class BlogPostRepository:
    def __init__(self, model_mapper: BlogPostMapper):
        self.model_mapper = model_mapper

    def save(self, entity: BlogPost) -> BlogPost:
        instance: BlogPostModel = self.model_mapper.to_instance(entity=entity)
        instance.save()
        return self.model_mapper.to_entity(instance=instance)

    def get_by_id(self, id: int) -> BlogPost:
        instance = BlogPostModel.objects.get(id=id)
        return self.model_mapper.to_entity(instance=instance)

    def delete(self, id: int):
        BlogPostModel.objects.filter(id=id).delete()

    def list_all(self) -> list[BlogPost]:
        instances = BlogPostModel.objects.all()
        return self.model_mapper.to_entity_list(instances=instances)

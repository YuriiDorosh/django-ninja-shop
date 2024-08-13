import uuid
from abc import (
    ABC,
    abstractmethod,
)


class BaseGenerateArticleService(ABC):
    @abstractmethod
    def generate_article(self, article: str) -> str:
        ...


class GenerateUuidArticleService(BaseGenerateArticleService):
    def generate_article(self, article: str) -> str:
        return str(uuid.uuid4())

import pytest
from utils import search_for_posts

pk_parameters = [
    "еда",
    "елки",
    "лампочка",
]


@pytest.mark.parametrize("user_query", pk_parameters)
def test_search_for_posts(user_query):
    # тесты для страницы с вхождением слова в пост
    search_posts = search_for_posts(user_query)
    assert len(search_posts) > 0


def test_search_for_posts_index_error():
    # возможная ошибка
    with pytest.raises(IndexError):
        search_for_posts("christmas")

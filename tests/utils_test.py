import pytest
from utils import get_posts_by_user, get_post_by_pk, get_comments_by_post_id

posts_parameters = [
    ("leo", "leo"),
    ("johnny", "johnny"),
    ("hank", "hank"),
]


@pytest.mark.parametrize("user_name, data_poster_name", posts_parameters)
def test_get_posts_by_user(user_name, data_poster_name):
    # тесты для страницы с определенным username
    assert get_posts_by_user(user_name)[1]['poster_name'] == data_poster_name


def test_get_posts_by_user_index_error():
    # возможная ошибка
    with pytest.raises(IndexError):
        get_posts_by_user("julia")






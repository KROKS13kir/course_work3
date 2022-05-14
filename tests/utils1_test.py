import pytest
from utils import get_comments_by_post_id, get_posts_by_user

post_id_parameters = [
    (1, 1),
    (5, 5),
    (7, 7),
]


@pytest.mark.parametrize("input_post_id, post_id", post_id_parameters)
def test_get_posts_by_user(input_post_id, post_id):
    #тесты для страницы с post_pk
    assert get_comments_by_post_id(input_post_id)[0]['post_id'] == post_id


def test_get_comments_by_post_id_index_error():
    # возможная ошибка
    with pytest.raises(IndexError):
        get_comments_by_post_id(25)

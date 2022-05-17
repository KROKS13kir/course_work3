import pytest
from utils import get_post_by_pk

pk_parameters = [
    (1, 1),
    (2, 2),
    (5, 5),
]


@pytest.mark.parametrize("user_pk, pk", pk_parameters)
def test_get_posts_by_user(user_pk, pk):
    # тесты для страницы с pk
    assert get_post_by_pk(user_pk)['pk'] == pk


def test_get_post_by_pk_index_error():
    # возможная ошибка
    with pytest.raises(IndexError):
        get_post_by_pk(88)

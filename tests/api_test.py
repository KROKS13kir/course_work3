from run import app



class TestApi:
    def test_app_all_posts_status_code(self):
        #тестим все посты на соответсвие ключей и типа-список
        response = app.test_client().get('/api/posts', follow_redirects=True)
        keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        first_keys = set(response.json[0].keys)
        assert type(response.json) == list
        assert keys == first_keys


    def test_app_one_post_status_code(self):
        #тестим пост на соответсвие ключей и типа-словарь
        keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        response = app.test_client().get('/api/post/2', follow_redirects=True)
        first_keys = set(response.json[0].keys)
        assert type(response.json) == dict
        assert keys == first_keys

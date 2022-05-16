import json
import re



def get_posts_all():
    with open("datas/data.json", "r", encoding="utf-8") as search_file:
        posts_mas = json.load(search_file)
    return posts_mas


def get_posts_by_user(user_name):
    all_posts = get_posts_all()
    result = []
    for post in all_posts:
        if user_name.lower() == post["poster_name"]:
            result.append(post)
    if len(result) == 0:
        raise IndexError("Такого имени нет в списке")
    return result



def get_comments_by_post_id(post_id):
    with open("datas/comments.json", "r", encoding="utf-8") as search_file:
        posts_mas = json.load(search_file)
    result = []
    for post in posts_mas:
        if post_id == post["post_id"]:
            result.append(post)
    if len(result) == 0:
        raise IndexError("Такого id нет в списке")
    return result


def search_for_posts(query):
    all_posts = get_posts_all()
    result_posts = []
    counter = 0
    for post in all_posts:
        if re.search(r'\b' + query.lower() + r'\b', post['content']):
            result_posts.append(post)
            counter += 1
        if counter == 10:
            break
    if len(result_posts) == 0:
        raise IndexError("Поста с такими словами не существует")
    return (result_posts, counter)


def get_post_by_pk(pk):
    all_posts = get_posts_all()
    for post in all_posts:
        if pk == post['pk']:
            return post
    raise IndexError("Такого pk нет в списке")




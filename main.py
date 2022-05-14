import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort

from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logger = logging.getLogger("basic")


@main_blueprint.route('/', methods=['GET'])
def profile_page():
    #главная страничка всех постов
    logger.debug("Все данные запрошены")
    try:
        all_posts = get_posts_all()
        return render_template("index.html", posts=all_posts)
    except:
        return "Что-то пошло не так"


@main_blueprint.route('/posts/<int:post_id>/', methods=['GET'])
def one_post_page(post_id):
    #страница поста с определенным pk
    logger.debug(f"Запрошен пост под номером {post_id}")
    try:
        post = get_post_by_pk(post_id)
        comments_to_one_post = get_comments_by_post_id(post_id)
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template('error.html', error=error)
    except BaseException as e:
        return render_template("error.html", error="неизвестная ошибка")
    else:
        if post is None:
            abort(404)

    length_of_comments = len(comments_to_one_post)
    return render_template("post.html", comments=comments_to_one_post, post=post, length_of_comments=length_of_comments)


@main_blueprint.route('/search/')
def search_page():
    #посты, в которые входит одно слово
    logger.debug("Все данные запрошены")
    try:
        s = request.args.get("s")
        all_posts = search_for_posts(s)
        return render_template("search.html", posts=all_posts[0], s=s, count_posts=all_posts[1])
    except:
        return "Что-то пошло не так"


@main_blueprint.route('/users/<string:username>/')
def one_user_page(username):
    #посты определенного пользователя
    logger.debug("Все данные запрошены")
    try:
        posts_by_username = get_posts_by_user(username)
        return render_template("user-feed.html", posts=posts_by_username)
    except:
        return "Что-то пошло не так"
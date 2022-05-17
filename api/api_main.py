import logging

from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)

logger = logging.getLogger("basic")

@api_blueprint.route('/api/posts/')
def posts_all():
    #все посты api
    logger.debug("Запрошены посты через API")
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>/')
def posts_post_id(post_id):
    # один пост api
    logger.debug(f"Запрошен пост c pk {post_id} через API")
    post = get_post_by_pk(post_id)
    return jsonify(post)

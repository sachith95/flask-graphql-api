from .models import Post
from ariadne import convert_kwargs_to_snake_case
import logging




def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        logging.debug('This is a debug message', posts)
        payload = {
            'posts': posts,
            'success': True
        }
    except Exception as e:
        payload = {
            'message': [str(e)],
            'success': False
        }
    return payload

@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    logging.debug(id)
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload
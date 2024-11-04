from flask import Blueprint, request, jsonify
from shared.models import Post, Hashtag
from shared.utils.db_utils import db

post_bp = Blueprint('post', __name__)

@post_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(
        caption=data.get('caption'),
        image_url=data.get('image_url'),
        video_url=data.get('video_url')
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201

@post_bp.route('/hashtags', methods=['POST'])
def create_hashtag():
    data = request.json
    new_hashtag = Hashtag(name=data.get('name'))
    db.session.add(new_hashtag)
    db.session.commit()
    return jsonify(new_hashtag.to_dict()), 201
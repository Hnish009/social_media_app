from flask import request, jsonify
from shared.models import Post, User, Hashtag

def search():
    query = request.args.get('query')
    posts = Post.query.filter(Post.caption.contains(query)).all()
    users = User.query.filter(User.username.contains(query)).all()
    hashtags = Hashtag.query.filter(Hashtag.name.contains(query)).all()
    
    return jsonify({
        'posts': [post.to_dict() for post in posts],
        'users': [user.to_dict() for user in users],
        'hashtags': [hashtag.to_dict() for hashtag in hashtags]
    })
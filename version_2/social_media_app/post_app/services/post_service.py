import re
from shared.models.post_model import Post
from shared.utils.db_utils import db
from post_app.models.hashtag_model import Hashtag
from post_app.models.like_model import Like
from post_app.models.comment_model import Comment

def extract_hashtags(content):
    return re.findall(r'#\w+', content)


class PostService:
    @staticmethod
    def create_post(user_id, content):
        new_post = Post(user_id=user_id, content=content)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.filter_by(post_id=post_id).first()

    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def update_post(post_id, new_content):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            post.content = new_content
            db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
        return post
    
    @staticmethod
    def create_post(user_id, content):
        hashtags = extract_hashtags(content)
        post = Post(user_id=user_id, content=content)
        db.session.add(post)
        db.session.commit()

        for tag in hashtags:
            hashtag = Hashtag(tag=tag, post_id=post.id)
            db.session.add(hashtag)
        db.session.commit()
        return post
    
    @staticmethod
    def search_posts(query):
         return Post.query.filter(Post.content.ilike(f'%{query}%')).all()
    
    @staticmethod
    def like_post(user_id, post_id):
        like = Like(user_id=user_id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
        return like

    @staticmethod
    def add_comment(user_id, post_id, content):
        comment = Comment(user_id=user_id, post_id=post_id, content=content)
        db.session.add(comment)
        db.session.commit()
        return comment

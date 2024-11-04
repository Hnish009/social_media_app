from shared.models.post_model import Post
from shared.utils.db_utils import db

class PostService:
    @staticmethod
    def create_post(user_id, content, hashtags=None, media_url=None):
        new_post = Post(user_id=user_id, content=content, hashtags=hashtags, media_url=media_url)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    # Add a method to search posts by hashtags
    @staticmethod
    def search_posts_by_hashtag(hashtag):
        return Post.query.filter(Post.hashtags.like(f'%{hashtag}%')).all()
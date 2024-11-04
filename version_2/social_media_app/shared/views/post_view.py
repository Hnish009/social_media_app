class PostView:
    @staticmethod
    def render_post(post):
        return {
            "post_id": post.post_id,
            "user_id": post.user_id,
            "content": post.content,
            "hashtags": post.hashtags,
            "media_url": post.media_url,  
            "created_at": post.created_at,
            "updated_at": post.updated_at
        }
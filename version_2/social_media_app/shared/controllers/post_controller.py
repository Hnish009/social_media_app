from flask import request
from post_app.services.post_service import PostService
from post_app.views.post_view import PostView

class PostController:
    @staticmethod
    def create_post():
        data = request.get_json()
        user_id = data.get('user_id')
        content = data.get('content')
        hashtags = data.get('hashtags') 
        media_url = data.get('media_url') 

        post = PostService.create_post(user_id, content, hashtags, media_url)
        return PostView.render_success('Post created successfully', post.post_id), 201
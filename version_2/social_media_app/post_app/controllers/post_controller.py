from flask import request
from post_app.services.post_service import PostService
from post_app.views.post_view import PostView

class PostController:
    @staticmethod
    def get_all_posts():
        posts = PostService.get_all_posts()
        return PostView.render_posts(posts), 200

    @staticmethod
    def get_post(post_id):
        post = PostService.get_post_by_id(post_id)
        if not post:
            return PostView.render_error('Post not found'), 404
        return PostView.render_post(post), 200

    @staticmethod
    def create_post():
        data = request.get_json()
        user_id = data.get('user_id')
        content = data.get('content')

        post = PostService.create_post(user_id, content)
        return PostView.render_success('Post created successfully', post.post_id), 201

    @staticmethod
    def update_post(post_id):
        data = request.get_json()
        new_content = data.get('content')

        post = PostService.update_post(post_id, new_content)
        if post:
            return PostView.render_success('Post updated successfully', post.post_id), 200
        return PostView.render_error('Post not found'), 404

    @staticmethod
    def delete_post(post_id):
        post = PostService.delete_post(post_id)
        if post:
            return PostView.render_success('Post deleted successfully', post.post_id), 200
        return PostView.render_error('Post not found'), 404

    @staticmethod
    def search_posts():
        query = request.args.get('query')
        posts = PostService.search_posts(query)
        return PostView.render_posts(posts), 200
    

    @staticmethod
    def like_post(post_id):
        user_id = request.args.get('user_id')  
        like = PostService.like_post(user_id, post_id)
        return PostView.render_success('Post liked successfully', like.id), 201

    @staticmethod
    def comment_on_post(post_id):
        data = request.get_json()
        user_id = data.get('user_id') 
        content = data.get('content')

        comment = PostService.add_comment(user_id, post_id, content)
        return PostView.render_success('Comment added successfully', comment.id), 201
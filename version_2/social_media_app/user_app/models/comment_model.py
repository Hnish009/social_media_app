from shared.utils.db_utils import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

    user = db.relationship('User', backref='comments')
    post = db.relationship('Post', backref='comments')
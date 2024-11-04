from shared.utils.db_utils import db  

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    user = db.relationship('User', backref='likes')
    post = db.relationship('Post', backref='likes')

    def __repr__(self):
        return f"<Like user_id={self.user_id} post_id={self.post_id}>"
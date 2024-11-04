from shared.utils.db_utils import db

class Hashtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    post = db.relationship('Post', backref='hashtags')

    def __repr__(self):
        return f"<Hashtag {self.tag}>"
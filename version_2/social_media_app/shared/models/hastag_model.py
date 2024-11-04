from shared.utils.db_utils import db

class Hashtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    posts = db.relationship('Post', secondary='post_hashtag', backref='hashtags')

# shared/models/post_hashtag.py
post_hashtag = db.Table('post_hashtag',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('hashtag_id', db.Integer, db.ForeignKey('hashtag.id'))
)
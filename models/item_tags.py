from db import db


class ItemTags(db.Model):
    __tablename__ = "item_tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))

    #item = db.relationship("ItemModel", back_populates="tags")
    #tag = db.relationship("TagModel", back_populates="items")
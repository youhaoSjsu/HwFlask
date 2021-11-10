from city import db


class User(db.Model):
    
    city_name = db.Column(db.String(64), unique=True, nullable=False)
    city_rank = db.Column(db.Integer, unique=True, nullable=False)
    is_visited = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"City('{self.city_name}', {self.city_rank}, {self.is_visited})"
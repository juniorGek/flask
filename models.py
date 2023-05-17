from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    articles = db.relationship('Article', backref='categorie', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'description': self.description
        }

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    description = db.Column(db.String(200))
    prix = db.Column(db.Float)
    quantité = db.Column(db.Integer)
    categorie_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'description': self.description,
            'prix': self.prix,
            'quantité': self.quantité,
            'categorie_id': self.categorie_id
        }

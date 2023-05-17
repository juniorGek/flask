from flask import request, jsonify
from app import app, db
from models import Article, Category

@app.route('/categories', methods=['POST'])
def add_category():
    new_category = Category(nom=request.json['nom'], 
                            description=request.json['description'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.serialize()), 201

@app.route('/articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    return jsonify([e.serialize() for e in articles])

@app.route('/articles/<id>', methods=['GET'])
def get_article(id):
    article = Article.query.get(id)
    if article is None:
        return "Article not found", 404
    return jsonify(article.serialize())

@app.route('/articles', methods=['POST'])
def add_article():
    new_article = Article(nom=request.json['nom'], 
                          description=request.json['description'], 
                          prix=request.json['prix'], 
                          quantité=request.json['quantité'],
                          categorie_id=request.json['categorie_id'])
    db.session.add(new_article)
    db.session.commit()
    return jsonify(new_article.serialize()), 201

@app.route('/articles/<id>', methods=['PUT'])
def update_article(id):
    article = Article.query.get(id)
    if article is None:
        return "Article not found", 404
    article.nom = request.json['nom']
    article.description = request.json['description']
    article.prix = request.json['prix']
    article.quantité = request.json['quantité']
    article.categorie_id = request.json['categorie_id']
    db.session.commit()
    return jsonify(article.serialize())

@app.route('/articles/<id>', methods=['DELETE'])
def delete_article(id):
    article = Article.query.get(id)
    if article is None:
        return "Article not found", 404
    db.session.delete(article)
    db.session.commit()
    return '', 204

@app.route('/articles/search', methods=['GET'])
def search_articles():
    keyword = request.args.get('keyword', '')
    articles = Article.query.filter(Article.description.contains(keyword)).all()
    return jsonify([e.serialize() for e in articles])


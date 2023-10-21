from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    supername = db.Column(db.String(255))
    created_at = db.Column(db.DateTime())
    updated_at = db.column(db.DateTime())

    powers = db.relationship('HeroPower', backref='heroes')

    def __repr__(self):
        return f'<Hero {Hero.name} is a beast>'


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255))
    hero_id = db.Column(db.Integer(), db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer(), db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime())
    updated_at = db.column(db.DateTime())

    power = db.relationship('Power', backref='hero_powers')
    hero = db.relationship('Hero', backref='hero_powers')

    def __repr__(self):
        return f'<HeroPower {HeroPower.strength}>'

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime())
    updated_at = db.column(db.DateTime())

    def __repr__(self):
        return f'<Power {Power.name}>'
from projeto import db, login_manager
from projeto import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=30), nullable=False, unique=True)
    usuario = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    senha = db.Column(db.String(length=15), nullable=False, unique=True)
    uploads = db.relationship('Uploads', backref='dono_user', lazy=True)

    @property
    def senhacrip(self):
        return self.senhacrip
    
    # Faz o set do atributo senhacrip. Ele criptografa a senha para que ela seja inserida no banco de forma segura.
    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8')

    # Converte a senha criptografada para o normal e a compara com uma outra senha. Deve-se chamar esse método ao realizar o login do usuário.
    def converte_senha(self, senha_texto_claro):
        return bcrypt.check_password_hash(self.senha, senha_texto_claro)


class Uploads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary, nullable=False)
    usuario = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, data):
        self.data = data
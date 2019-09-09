from app import create_app
from app.extensions import db

app = create_app()
db.create_all(app=app)
app.app_context().push()

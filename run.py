from app.db.db_init import iniciar_db
from app.main import window
from app.views.home import show_dashboard

iniciar_db()
show_dashboard(window)

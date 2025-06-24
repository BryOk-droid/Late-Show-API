from server.app import db, create_app
from server.models import Guest, Episode

app = create_app()

with app.app_context():
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()

    guest = Guest(name="Kevin Hart", occupation="Comedian")
    episode = Episode(date="2025-06-20", number=1)

    db.session.add(guest)
    db.session.add(episode)
    db.session.commit()

    print("Database seeded.")

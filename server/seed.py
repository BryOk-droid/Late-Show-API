from server.app import db, create_app
from server.models import Guest, Episode, Appearance

app = create_app()

with app.app_context():
    
    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()

    
    guest1 = Guest(name="Kevin Hart", occupation="Comedian")
    guest2 = Guest(name="Zendaya", occupation="Actress")
    guest3 = Guest(name="Trevor Noah", occupation="TV Host")

   
    episode1 = Episode(date="2025-06-20", number=1)
    episode2 = Episode(date="2025-06-21", number=2)

    
    db.session.add_all([guest1, guest2, guest3, episode1, episode2])
    db.session.commit()

   
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode1.id)
    appearance3 = Appearance(rating=5, guest_id=guest3.id, episode_id=episode2.id)

    db.session.add_all([appearance1, appearance2, appearance3])
    db.session.commit()

    print("✅ Database seeded with guests, episodes, and appearances.")

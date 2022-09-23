from app.models import db, Post, User
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_posts():
    sephiroth = User(
        profile_pic='https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/02/Sephiroth-Final-Fantasy.jpg',
        name='Sephiroth',
        username='OneWingedAngel',
        email='seph@aa.io',
        password='password',
        bio='The Reunion Is Nothing To Fear.',
        place='New York City, New York',
        birthday=datetime(1990, 10, 11),
        banner_pic='https://static1.srcdn.com/wordpress/wp-content/uploads/2020/03/Sephiroth-Midgar-Cover-Final-Fantasy-VII-Remake.jpg',
        joined=datetime(2010, 5, 8)
        )

    tifa = User(
        profile_pic='https://oyster.ignimgs.com/mediawiki/apis.ign.com/final-fantasy-vii-remake/9/94/Final-Fantasy-VII-Remake-Tifa.jpg',
        name='Tifa',
        username='glovegirl',
        email='Tifa@aa.io',
        password='password',
        birthday=datetime(1995, 8, 20),
        place='Midgar',
        bio="I'll Be Fine. You've Seen How Much Ass I Can Kick.",
        banner_pic='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1f8d9181-e997-4dbf-a95b-4bed86f14cca/defhkep-1ade3238-febc-4a95-950d-6a03f2b9ef7e.jpg',
        joined=datetime(2009, 10, 28)
        )
    aerith = User(
        profile_pic='https://d3fd5j8wprxn3h.cloudfront.net/wp-content/uploads/2020/04/final-fantasy-7-remake-aerith-final-fantasy-vii-remake-aerith.jpg',
        name='Aerith',
        username='LastoftheCetra',
        email='aerith@aa.io',
        password='password',
        place='Midgar',
        birthday=datetime(1996, 7, 10),
        bio='We Need To Make The Most Of The Time We Have. To Live Our Lives The Way We Wanna Live.n',
        joined=datetime(2015, 10, 16),
        banner_pic='https://cdn.gamer-network.net/2020/usgamer/Final-Fantasy-7-Remake_Post-Review_Screenshot11.jpg'
        )

    db.session.add(sephiroth)
    db.session.add(tifa)
    db.session.add(aerith)



    demoPost = Post(
        body='My name is demo and this is my first post',
        # likes=3,
        reposts=2,
        images='https://www.theedadvocate.org/wp-content/uploads/2016/02/board-361516_960_720.jpg',
        user_id=1
        )
    marniePost = Post(
        body='Hello World, I am Cloud',
        # likes=5,
        reposts=4,
        user_id=2
        )
    bobbiePost = Post(
        body='My name bobbie bushay',
        # likes=6,
        reposts=5,
        images='https://www.musictoyourhome.com/wp-content/uploads/2021/04/8-Easy-Guitar-Songs-For-Every-Beginner.jpg',
        user_id=3
        )

    db.session.add(demoPost)
    db.session.add(marniePost)
    db.session.add(bobbiePost)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()

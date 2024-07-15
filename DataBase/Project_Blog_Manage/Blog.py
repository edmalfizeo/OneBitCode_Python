from connection_orm import base, engine, session
from User import User
from Post import Post

# Create a table
base.metadata.create_all(bind=engine)


# Function for showing option menu
def show_menu():
    print('1. Create a new user')
    print('2. Create a new post')
    print('3. Show all users and posts')
    print('4. Exit')
    return int(input('Enter your choice: '))


# Function for creating a new user
def create_user():
    print('Create a new user')
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print('User created successfully!')


# Function for creating a new post
def create_post():
    print('Create a new post')
    title = input('Enter your title: ')
    content = input('Enter your content: ')
    user_id = int(input('Enter your user id: '))
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        post = Post(title=title, content=content, creator=user)
        session.add(post)
        session.commit()
        print('Post created successfully!')
    else:
        print('User not found!')


# Function for showing all users and posts
def show_all():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f'User: {user.name}, Email: {user.email}')
        for post in user.posts:
            print(f'Post: {post.title}')
            print(f'Content: {post.content}')
            print('-----------------------')
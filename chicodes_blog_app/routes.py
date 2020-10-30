# Import the app variable from the init
from chicodes_blog_app import app, db

# Import specific packages from flask
from flask import render_template, request, redirect, url_for 

# import our form(s)
from chicodes_blog_app.forms import UserInfoForm, LoginForm, PostForm

# import of Our Model(s)
from chicodes_blog_app.models import User, Post, check_password_hash

# import for Flask Login functions - login_required
# login_user, current_user, logout_user
from flask_login import login_required, login_user, current_user, logout_user 

# Default Home Route 
@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', user_posts = posts)

@app.route('/test')
def testRoute():
    names = ['Robert', 'David', 'Bill', 'Jessy']
    return render_template('test.html', list_names = names)

# GET == gathering info
# POST == sending info
@app.route('/register', methods = ['GET', 'POST'])
def register():
    # init our form
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # print the data to the server that comes from the form
        print(username,email,password)

        # Creation/Init of our User Class (aka Model)
        user = User(username, email, password)

        # Open a connection to the database
        db.session.add(user)

        # Commit all data to the database
        db.session.commit()

    return render_template('register.html', user_form = form)
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        # check the password of the newly found user
        # and validate the password against the hash value
        # inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            # Redirect user
            return redirect(url_for('home'))
        else:
            # Redirect User to login route
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Creation of posts route
@app.route('/posts', methods = ['GET', 'POST'])
@login_required
def posts():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id 
        post = Post(title, content,user_id)

        db.session.add(post)

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('posts.html', post_form = form)

# post detail route to display info about a post
@app.route('/posts/<int:post_id>')
@login_required
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/posts/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_update(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()

    if request.method == 'POST' and form.validate():
        title = form.title.data 
        content = form.content.data  
        user_id = current_user.id 

        # Update the Database with the new Info
        post.title = title 
        post.content = content 
        post.user_id = user_id 

        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post_update.html', update_form=form)


@app.route('/posts/delete/<int:post_id>', methods=['GET', 'POST', 'DELETE'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))

from flask import Flask, render_template, request, abort
from crud_read_flask_2907.repository import PostsRepository

app = Flask(__name__)

repo = PostsRepository(50)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/posts') # список постов
def list_posts():
    posts = repo.content()  # получаем список постов
    page = request.args.get('page', 1, type=int) # получаем номер страницы. Адрес типа ?page=3&per=3. По умолч. 1
    limit = 5 #request.args.get('per', 5, type=int) # получаем кол-во постов на стр. Адрес типа ?page=3&per=3. По умолч. 5
    total_pages = int(len(posts)/limit)
    print(total_pages)
    offset = (page - 1) * limit
    slice_of_post = posts[offset:page*limit]
    return render_template('posts/index.html', posts=slice_of_post, page=page, total_pages=total_pages )


@app.route('/posts/<slug>') # конкретный пост
def post(slug):
    # posts = repo.content()
    post = repo.find(slug)
    if post is None: 
        return 'Page not found', 404 #abort(404)  # Возвращает HTTP-статус 404
    else:
        return render_template('posts/show.html', post=post)


# END

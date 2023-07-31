from crud_read_flask_2907.data import generate


class PostsRepository:
    def __init__(self, size):
        self.posts = generate(size)

    def content(self):
        return self.posts

    def find(self, slug):
        return next((post for post in self.posts if slug == post['slug']), None)

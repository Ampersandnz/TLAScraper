class Chapter:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.text = ""

    def set_body_text(self, text):
        self.text = text

    def get_post_id(self):
        return self.url.split('-')[-1]

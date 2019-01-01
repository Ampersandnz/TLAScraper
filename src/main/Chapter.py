class Chapter:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.text = ""

    def set_body_text(self, text):
        self.text = text

    def get_post_id(self):
        if "threads" in self.url:
            return self.url.split('-')[-1]
        elif "posts" in self.url:
            return self.url.split('/')[-2]
        else:
            print(f"Unparsable url! {self.url}")
            return None

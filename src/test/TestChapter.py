import unittest

from Chapter import Chapter


class TestChapter(unittest.TestCase):
    PROLOGUE_POST = "https://forums.spacebattles.com/threads/the-last-angel.244209/#post-9354450"

    def test_scrape_chapter_contents(self):
        chapter = Chapter("Prologue", "https://forums.spacebattles.com/threads/the-last-angel.244209/#post-9354450")
        post_id = chapter.get_post_id()
        self.assertEqual("post-9354450", post_id)


if __name__ == '__main__':
    unittest.main()

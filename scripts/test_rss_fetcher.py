import unittest
from rss_fetcher import is_safe_url, fetch_article

class TestSSRFPrevention(unittest.TestCase):
    def test_safe_urls(self):
        self.assertTrue(is_safe_url("http://example.com"))
        self.assertTrue(is_safe_url("https://google.com"))

    def test_unsafe_urls(self):
        self.assertFalse(is_safe_url("http://localhost"))
        self.assertFalse(is_safe_url("http://127.0.0.1"))
        self.assertFalse(is_safe_url("http://192.168.1.1"))
        self.assertFalse(is_safe_url("http://10.0.0.1"))
        self.assertFalse(is_safe_url("http://172.16.0.1"))
        self.assertFalse(is_safe_url("http://169.254.169.254/latest/meta-data/"))
        self.assertFalse(is_safe_url("file:///etc/passwd"))
        self.assertFalse(is_safe_url("ftp://example.com"))
        self.assertFalse(is_safe_url("http://0.0.0.0"))

    def test_fetch_article_unsafe_url(self):
        # Should return empty string without actually fetching
        self.assertEqual(fetch_article("http://127.0.0.1"), "")
        self.assertEqual(fetch_article("http://localhost"), "")

if __name__ == "__main__":
    unittest.main()

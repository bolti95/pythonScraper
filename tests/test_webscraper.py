from pathlib import Path
import unittest


from webscraper.webscraper import scrape
# import webscraper
# from webscraper.webscraper import scrape

class WebScraperTests(unittest.TestCase):
    def test_function(self):
        scrape
        self.assertEqual(scrape, True)
    

# if we run module directly, run code in this conditional
if __name__ == "__main__":
    unittest.main()

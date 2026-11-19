"""US-04 tests. Run all tests with:  python -m unittest -v"""

from test_library import LibraryTestCase


class TestSearch(LibraryTestCase):  # US-04
    def test_search_books(self):
        from books import search_books
        self.assertEqual([b["id"] for b in search_books(self.db, "sommerville")], ["B3"])
        self.assertEqual(search_books(self.db, "no such book"), [])

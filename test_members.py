"""US-05 tests. Run all tests with:  python -m unittest -v

The test that a member with a loan cannot be removed needs loans.py
(US-06), so add it when US-06 is built.
"""

from test_library import LibraryTestCase


class TestMembers(LibraryTestCase):  # US-05
    def test_add_member_and_reject_duplicate_email(self):
        from members import add_member
        add_member(self.db, "Sara Ali", "sara@example.com")
        with self.assertRaises(ValueError):
            add_member(self.db, "Sara Two", "SARA@example.com")

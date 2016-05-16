"""Demo basics of using test environment."""

from framework.testbase import BaseTestCase


class ExampleTestCase2(BaseTestCase):
    """Demo basics of using test environment."""

    def test_foo(self):
        """Another test demo in diff class for a better report."""
        self.log.info("executing ExampleTestCase2.test_foo")
        self.assertTrue(1)

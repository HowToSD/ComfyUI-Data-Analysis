import os
import sys
import unittest


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from cda.py_kv_int_create import PyKvIntCreate

class TestPyKvIntCreat(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PyKvIntCreate()
        self.data = [
            {"key": "a", "value": 12345678}
        ]

    def test_create_key_value_pair(self):
        """Test key-value pair creation."""
        retval = self.node.f(key=self.data[0]["key"], value=self.data[0]["value"])[0]
        self.assertEqual({self.data[0]["key"]: self.data[0]["value"]}, retval)


if __name__ == "__main__":
    unittest.main()


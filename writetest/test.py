import unittest
from unittest.mock import patch

from func import Application


class ApplicationTest(unittest.TestCase):
    app = Application()

    def test_parent(self):
        with patch('func.Application.child') as mock_child:
            mock_child.return_value = None
            self.parent()
            self.app.parent(9)
            # mock_child.assert_called_once_with(9)


if __name__ == '__main__':
    unittest.main()

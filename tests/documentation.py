"""An entry point for running the doctests."""

import manuel.codeblock
import manuel.doctest
import manuel.testing
import unittest
import doctest


def test_suite():
    """Construct a Manuel-enhanced test suite for running the doctests."""
    m = manuel.doctest.Manuel(optionflags=doctest.ELLIPSIS)
    m += manuel.codeblock.Manuel()
    return manuel.testing.TestSuite(m, '../tutorial.rst')


if __name__ == '__main__':  # pragma: no cover
    unittest.TextTestRunner().run(test_suite())

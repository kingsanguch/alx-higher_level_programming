#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Overrides the equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the inequality operator"""
        return super().__eq__(other)

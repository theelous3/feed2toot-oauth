#!/usr/bin/env python3
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Launch Feed2toot"""

import sys
from feed2toot.main import Main


class Feed2Toot(object):
    """Feed2toot class"""

    def __init__(self):
        """Constructor of the Feed2Toot class"""
        self.main()

    def main(self):
        """main of the Feed2Toot class"""
        Main()


if __name__ == "__main__":
    Main()
    sys.exit(0)

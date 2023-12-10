#!/usr/bin/python3
"""This is a Test for the console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """This is a Class test console"""

    def create(self):
        """Create an instance"""
        return HBNBCommand()

    def test_quit(self):
        """
        Test for the method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """
        Test for the method EQF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))

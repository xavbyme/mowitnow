#!/usr/local/bin/python3.7
# -*- coding: cp1252 -*-
# Module de teste
from unittest import TestCase

# Module a tester
import tools

# Test du split
class TestSplitSpace(TestCase):
    # Teste si le resultat du parsing est une liste
    def test_is_instance(self):
        strToParse = "X E B I A"
        s = tools.splitSpace(strToParse)
        self.assertTrue(isinstance(s, list))

    # Teste si la longueur du split est bien de 5 en splitant la chaine en entree
    def test_is_well_split(self):
        strToParse = "X E B I A"
        s = tools.splitSpace(strToParse)
        self.assertEqual(len(s), 5)


# Test du parser d arguments
class TestParser(TestCase):
    # Initialisation du parser
    def setUp(self):
        self.parser = tools.getArguments()

    # Teste de la recuperation de l argument
    def test_something(self):
        parsed = self.parser.parse_args(["--file", "xebia.txt"])
        self.assertEqual(parsed.file, "xebia.txt")

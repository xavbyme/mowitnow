#!/usr/local/bin/python3.7
# -*- coding: cp1252 -*-

import argparse
import sys

# Fonction de parsing et récupération des arguments
def getArguments():

    parser = argparse.ArgumentParser(
        prog="MowItNow_Controller",
        description="Controle un ensemble de tondeuses MowItNow.",
    )

    # Argument contenant le path complet du fichier de controle
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Nom du fichier dentree du programme contenant les instructions de controle.",
    )

    return parser


# Parser sur les espaces et retour chariot
def splitSpace(stringSplit):
    stringWtoN = stringSplit.rstrip("\n")
    arrayWtoSpace = stringWtoN.split()
    return arrayWtoSpace


# Sortie en erreur avec affichage de l erreur
def errorExit(error_message):
    sys.exit(error_message)

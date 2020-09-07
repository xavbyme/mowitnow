#!/usr/local/bin/python3.7
# -*- coding: cp1252 -*-

"""
SYNOPSIS
    MowItNow_Controller.py [-h,--help] [-f,--file]

DESCRIPTION
    Programme permettant de controler un ensemble de tondeuses MowItNow
    Specifications completes contenues dans le package - "ExerciceTechnique - La Tondeuse.pdf"

ARGUMENTS
    -h, --help			Show this help message and exit
    -f, --file			Path complet du fichier d'entree du programme contenant les instructions de controle	

AUTHOR
    Xavier RUIZ <ruiz.xvr@gmail.com>

GIT
	https://github.com/xavbyme/mowitnow.git

PYPI
	https://pypi.org/project/mowitnow

HISTORY
	1.0		XRU 15/10/2018	Packaging - Ajout des tests
	0.3		XRU	13/10/2018	Corrections de la classe mower - Ajout de la classe mowSwarm - Factorisation
	0.2		XRU	12/10/2018	Version fonctionnelle
	0.1 	XRU	12/10/2018	Versoion initiale - Structure - Git - Deploiement Pypi.org
"""

# Imports
import os
import sys

# Module contenant les classes
import mowitnow.mowers

# Module contenant les fonctions utilisees
import mowitnow.tools

# Main
if __name__ == "__main__":
    # Recuperation des arguments
    args = tools.getArguments()
    arrayArgs = args.parse_args()

    # Recuperation du path du fichier de controle
    filepath = arrayArgs.file

    # Initialisation de l index de l array de tondeuses
    indMower = 0

    # Instanciation d un essaim de tondeuses
    essaimTondeuse = mowers.mowSwarm()

    # Test de presence du fichier
    if not os.path.exists(filepath):
        tools.errorExit("Erreur : Fichier de controle introuvable.")

    # Ouverture du fichier de controle
    with open(filepath, "r") as fileReader:
        # Lecture du fichier ligne a ligne
        for num, line in enumerate(fileReader):
            # Parsing de la ligne extraite du fichier
            line = tools.splitSpace(line)

            # Case ligne 0 - taille de la matrice
            if num == 0:
                # Construction d une instance de field
                terrain = mowers.field(line)
                # Affichage des caracteristiques du terrain
                terrain.displayBorders()
            # Case ligne 1 - position initiale de la tondeuse
            elif (num % 2) == 1:
                # Instanciation d une tondeuse
                tondeuse = mowers.mower(terrain, indMower, line)
                # Affichage de la position
                tondeuse.displayPos()

            # Case ligne 2 - deplacement
            elif (num % 2) == 0:
                # Lecture du string d instructions de mouvements de la tondeuse
                for ch in line[0]:
                    # Instruction de mouvement
                    tondeuse.moveMower(ch)
                # Ajout d une tondeuse a l instance d essaim cree
                essaimTondeuse.addMow(tondeuse)
                # Incrementation de l indice necessaire a l array de tondeuses
                indMower += 1

    # Affichage de la position des tondeuses de l essaim
    essaimTondeuse.displaySwarm()

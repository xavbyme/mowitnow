MowItNow Controller
------------------

SYNOPSIS
    
    MowItNow_Controller.py [-h,--help] [-f,--file]               

DESCRIPTION
    
    Programme permettant de controler un ensemble de tondeuses MowItNow
    Specifications completes contenues dans le package - "ExerciceTechnique - La Tondeuse.pdf"

ARGUMENTS
    
    -h, --help          Show this help message and exit
    -f, --file          Path complet du fichier d'entree du programme contenant les instructions de controle

INPUT
    
    Le programme traite un fichier de contrôle qui contient:
        - 1ere ligne : Taille maximale du terrain
        - 2eme ligne : Position de la premiere tondeuse
        - 3eme ligne : Deplacements de lapremiere  tondeuse
        - 4eme ligne : Position de la seconde tondeuse
        - 5eme ligne : Deplacements de la seconde tondeuse
        Etc.

AUTHOR
    
    Xavier RUIZ <ruiz.xvr@gmail.com>

GIT
        
    https://github.com/xavbyme/mowitnow.git

PYPI
        
    https://pypi.org/project/mowitnow

HISTORY
        
        0.03    XRU     13/10/2018      Corrections de la classe mower - Ajout de la classe mowSwarm - Factorisation
        0.02    XRU     12/10/2018      Version fonctionnelle
        0.01    XRU     12/10/2018      Versoion initiale - Structure - Git - Deploiement Pypi.org

# ENSAE Programming Project 2024: Sliding Tile Solver

## Description
Ce projet consiste à développer une solution algorithmique pour résoudre le problème classique du réarrangement d'une grille de tuiles numérotées. L'objectif est de trouver la séquence minimale de mouvements pour organiser les tuiles dans l'ordre croissant, en respectant des règles de déplacement spécifiques.

Ce projet a été réalisé dans le cadre du cours de programmation en première année à l'ENSAE Paris, sous la supervision de [Patrick Loiseau](mailto:patrick.loiseau@inria.fr).

## Fonctionnalités principales
- **Génération aléatoire ou personnalisée** de grilles initiales.
- **Algorithmes de résolution optimisés**, incluant :
  - BFS (Breadth-First Search) pour garantir des solutions optimales.
  - A* pour une recherche plus rapide grâce à une heuristique adaptée.
- **Visualisation des étapes de résolution** via des sorties en ligne de commande.
- **Tests unitaires complets** pour valider chaque composante du projet.
- Documentation détaillée des choix algorithmiques et des résultats.

ensae-prog24/
│
├── main.py              # Script principal
├── grid.py              # Gestion de la grille et des mouvements
├── solver.py            # Implémentation des algorithmes de résolution
├── tests/               # Tests unitaires
│   ├── test_grid.py     # Tests pour la gestion de la grille
│   ├── test_solver.py   # Tests pour les algorithmes de résolution
├── README.md            # Documentation du projet
└── requirements.txt     # Fichier pour les dépendances (vide ou à compléter)



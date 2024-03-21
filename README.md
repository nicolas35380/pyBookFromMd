# pyBookFromMd

## Présentation rapide

Génération de livres, documentation ou ebook à partir de fichiers Markdown listés dans un fichier d'input (files.txt) et de Pandoc. Les paramètres sont facilement éditables pour faciliter la configuration.

## Mode d'emploi

1. Dans l'idéal, préfixer les fichiers *.md correspondants aux chapitre dans l'ordre de lecture : ``01-lorem``, ``02-ipsum``, etc. et les déposer dans le même répertoire que ``main.py``.
2. En bash, faire un ``ls *.md > files.txt`` pour générer le fichier d'entrée.
3. Dans le fichier ``main.py``, modifier les constantes définies en début de programme pour personnaliser le rendu.
4. Si le document contient différentes parties principales, intégrer les balises tex ``\part{Première partie : Lorem Ipsum}`` en début de fichier ``*.md`` de nouvelle partie.

## Pré requis

- [Pandoc](https://pandoc.org/) doit être installé et déclaré dans le PATH.
- [LaTeX](https://en.wikibooks.org/wiki/LaTeX/Installation#Distributions) doit être installé.
- Le template [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) doit être installé.

## Historique des versions

``v1.0.0`` : Publication initiale en ligne de commande. Paramétrage depuis les constantes dans ``main.py``. Utilisation d'un fichier d'entrée ``files.txt``.

## Todo

- [ ] Interface graphique tout en un pour execution simple et portable. (*en cours*)
- [ ] Dockerisation avec tout les pré requis pour accès externe.

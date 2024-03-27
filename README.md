# pyBookFromMd

## Présentation rapide

Génération de livres, documentation ou ebook à partir de fichiers Markdown listés dans un fichier d'input (files.txt) et de Pandoc. Les paramètres sont facilement éditables pour faciliter la configuration.

## Pré requis

- [Pandoc](https://pandoc.org/) doit être installé et déclaré dans le PATH.
- [LaTeX](https://en.wikibooks.org/wiki/LaTeX/Installation#Distributions) doit être installé.
- Le template [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) doit être installé.
- **[optionnel]** [Support Mermaid](https://github.com/raghur/mermaid-filter) : au besoin, installer le filtre Pandoc ``mermaid-filter`` avec la commande ``npm install --global mermaid-filter``. Enfin, dans ``config.ini`` : activer le support Mermaid en basculant ``MERMAID_SUPPORT`` à ``True``.

## Mode d'emploi

### Avec l'executable prêt à l'emploi

1. Téléchargez et dézippez l'archive ``pyBookFromMd.zip`` dans le répertoire de votre choix.
2. Dans l'idéal, préfixez les fichiers *.md correspondants aux chapitres dans l'ordre de lecture : ``01-lorem``, ``02-ipsum``, etc. et déposez dans le même répertoire que l'exécutable ``pyBookFromMd.exe``.
3. En bash, faites un ``ls *.md > files.txt`` pour générer le fichier d'entrée.
4. Dans le fichier ``config.ini``, modifiez les paramètres de génération pour personnaliser le rendu.
5. Si le document contient différentes parties principales, intégrer les balises TEX ``\part{Première partie : Lorem Ipsum}`` en début de fichier ``*.md`` de nouvelle partie.
6. Assurez-vous que les fichiers ``config.ini``, ``files.txt`` et éventuellement votre illustration de couverture (ou à défaut ``title-background.png``) soient bien présents dans le même répertoire que votre exécutable.
7. Éxecutez ``pyBookFromMd.exe``.
8. Ouvrez le PDF généré.

### Depuis les sources

1. Clonez le dépôt ou téléchargez l'archive contenant les sources et dézippez dans le répertoire de votre choix.
2. Dans l'idéal, préfixez les fichiers *.md correspondants aux chapitres dans l'ordre de lecture : ``01-lorem``, ``02-ipsum``, etc. et déposez les dans le même répertoire que les fichiers ``*.py``.
3. En bash, faites un ``ls *.md > files.txt`` pour générer le fichier d'entrée.
4. Dans le fichier ``config.ini``, modifiez les paramètres de génération pour personnaliser le rendu.
5. Si le document contient différentes parties principales, intégrer les balises TEX ``\part{Première partie : Lorem Ipsum}`` en début de fichier ``*.md`` de nouvelle partie.
6. Lancez main.py avec la commande ``python -m main.py``.
7. Ouvrez le PDF généré.

## Historique des versions

- ``v1.3.0`` : Passage des paramètres via fichier .INI pour packaging de la solution. Suppression de ``settings.py``.
- ``v1.2.0`` : Ajout du support de Mermaid avec ``mermaid-filter``.
- ``v1.1.0`` : Ajoute le support des Headers et Footers personnalisés. Légère refactorisation : séparation en plusieurs fichiers
  - **main.py** : fichier principal à executer.
  - **function.py** : définition des fonctions aditionnelles comme la lecture du fichier d'entrées et la fabriction de la ligne de commande de Pandoc.
  - **settings.py** : fichier de paramétrage. A modifier pour personnaliser le rendu.
- ``v1.0.0`` : Publication initiale en ligne de commande. Paramétrage depuis les constantes dans ``main.py``. Utilisation d'un fichier d'entrée ``files.txt``.

## Todo

- [x] Transformer ``settings.py`` en fichier de paramétrage externe en vue de distribuer un package ``*.exe``.
- [x] Évaluation l'intérêt de pypandoc pour le projet. [Pour référence](https://pypi.org/project/pypandoc/). Non pertinent.
- [ ] Dockerisation avec tout les pré requis pour accès externe. [Pour référence](https://github.com/dalibo/pandocker).

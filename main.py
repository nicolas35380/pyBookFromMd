"""
Objectif : Générer un PDF à partir des fichiers MD listés dans files.txt

Notice :
    1. Dans l'idéal, préfixer les fichiers *.md correspondants aux chapitre dans l'ordre de lecture : 01-lorem, 02-ipsum, etc. et les déposer dans le même répertoire que main.py
    2. En bash, faire un 'ls *.md > files.txt' pour générer le fichier d'entrée
    3. Dans le fichier courant main.py, modifier les constantes définies en début de programme pour personnaliser le rendu.
    4. Si le document contient différentes parties principales, intégrer les balises tex \part{Première partie : Lorem Ipsum} en début de fichier *.md de nouvelle partie

Étapes :
    1. [x] Définir les options via des constantes
    2. [x] Lire les input via files.txt : nom des fichiers et quantité
    3. [x] Construire les arguments avec ces inputs et ces constantes
    4. [x] Appeler PANDOC
    5. [ ] Refactoring en prévision de la création de l'UI ?
    6. [ ] Utiliser un framework graphique pour fabriquer une interface graphique ?
"""

import subprocess
import os

MD_REQUIREMENT_FILES = "files.txt"

# ---- PANDOC Options ----

## General Options
PDF_OUTPUT_NAME = "doc.pdf"             # output filename
TEMPLATE_NAME = "eisvogel"              # pdf theme
TOC_DEPTH = 2                           # depth of table of content
TOP_LEVEL_DIVISION = "chapter"          # part, chapter
CLASSOPTION = "oneside"                 # "oneside" for PDF, "" if printed
HIGHLIGHT_STYLE = "tango"               # 

## Title Page Options
TITLEPAGE_LOGO = ""            # path to an image that will be displayed on the title page, relative path only
LOGO_WIDTH = "20mm"                     # width of the logo. Specify the width with a (TeX) unit e.g. 100pt or 35mm, defaults to 35mm - see https://github.com/tweh/tex-units
TITLEPAGE_COLOR = "135AAD"              # background color of the title page
TITLEPAGE_TEXT_COLOR = "FFFFFF"         # text color of the title page, defaults to 5F5F5F
TITLEPAGE_RULE_COLOR = "112631"         # color of the rule on the top of the title page, defaults to 435488
TITLEPAGE_RULE_HEIGHT = 0               # height of the rule on the top of the title page (in points), defaults to 4
TITLEPAGE_BACKGROUND = "title-background.png"               # path to a background image for the title page. The background image is scaled to cover the entire page

## Any Pages Options
PAGE_BACKGROUND = ""                    # path to a background image for any page. The background image is scaled to cover the entire page
PAGE_BACKGROUND_OPACITY = ""            # the background image opacity, defaults to 0.2

## Metadata
METADATA_AUTHOR = "Nicolas PRENVEILLE"
METADATA_TITLE = "Formation Algorithmique"
METADATA_SUBJECT = "L'algorithmique est un pilier fondamental pour tout développeur souhaitant exceller dans le monde numérique. Avec ce programme, vous établirez une base solide pour réussir dans le secteur de la programmation."
METADATA_SUBTITLE = "Créer, analyser et améliorer des algorithmes sophistiqués"
METADATA_DATE = "2023-2024"

## Listing Options
LISTING_NO_PAGE_BREAK = "true"          # avoid page break inside listings, defaults to false (seems to be KO)


if __name__ == "__main__":

    # ---- Décompte des lignes de files.txt et sauvegarde des noms de fichiers dans une liste----
    file_list = []
    with open(MD_REQUIREMENT_FILES, "r") as fp:
        file_list = fp.read().splitlines()
        # print(f"Fichiers à traiter : {file_list}")
        # print(subprocess.list2cmdline(file_list))
        # print("Génération de l'argument : " + " ".join(file_list))
        # print(f"Total à traiter(s) : {len(file_list)}")

    # ---- Appel à PANDOC avec les arguments spécifiés
    """
    pandoc ./01-bases-de-lalgorithmie/01-renforcement-des-fondamentaux.md ./01-bases-de-lalgorithmie/02-introduction-aux-structures-de-donnees.md ./01-bases-de-lalgorithmie/03-algorithmes-de-tri-et-de-recherche.md ./01-bases-de-lalgorithmie/04-complexite-et-efficacite-des-algorithmes.md ./01-bases-de-lalgorithmie/05-introduction-la-programmation-dynamique-et-aux-graphes.md ./02-designs-pattern/01-apres-les-bases-de-lalgorithmique.md ./02-designs-pattern/02-importance-de-la-bonne-conception-de-logiciels.md 99-annexes01.md 99-annexes02.md 99-annexes03.md 99-annexes04.md -o doc.pdf --from markdown --template eisvogel -V geometry:margin=1in -N --toc --toc-depth=2  -V lang=fr-FR -V titlepage=true -V titlepage-color=6C2460 -V titlepage-text-color=FFFFFF -V titlepage-rule-color=74B92A -V toc-own-page=true -V book --top-level-division=chapter -V classoption=oneside --highlight-style=tango
    """

    cmd_line = "pandoc " + subprocess.list2cmdline(file_list) + f" -o {PDF_OUTPUT_NAME} --from markdown+raw_tex --template {TEMPLATE_NAME} -V geometry:margin=1in -N --toc --toc-depth={TOC_DEPTH}  -V lang=fr-FR -V titlepage=true -V titlepage-color={TITLEPAGE_COLOR} -V titlepage-text-color={TITLEPAGE_TEXT_COLOR} -V titlepage-rule-color={TITLEPAGE_RULE_COLOR} -V titlepage-rule-height={TITLEPAGE_RULE_HEIGHT} -V titlepage-logo={TITLEPAGE_LOGO} -V logo-width={LOGO_WIDTH} -V titlepage-background={TITLEPAGE_BACKGROUND} -V page-background={PAGE_BACKGROUND} -V page-background-opacity={PAGE_BACKGROUND_OPACITY} -V toc-own-page=true -V book --top-level-division={TOP_LEVEL_DIVISION} -V classoption={CLASSOPTION} -V listings-no-page-break={LISTING_NO_PAGE_BREAK} --highlight-style={HIGHLIGHT_STYLE} --metadata=author:\"{METADATA_AUTHOR}\" --metadata=title:\"{METADATA_TITLE}\" --metadata=subject:\"{METADATA_SUBJECT}\" --metadata=subtitle:\"{METADATA_SUBTITLE}\" --metadata=date:\"{METADATA_DATE}\""
    print("Ligne de commande : " + cmd_line)
    os.system(cmd_line)


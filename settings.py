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
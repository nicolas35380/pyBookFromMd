import subprocess
import os
from settings import *

# Open input file and read *.md
# return a list of *.md to append
def read_input_file(file):
    file_list = []
    with open(file, "r") as fp:
        file_list = fp.read().splitlines()
    return file_list

# Call to PANDOC and build PDF
# Return 0 for success, 1 for error (TODO)
def pdf_build(file_list):
    cmd_line = "pandoc " + subprocess.list2cmdline(file_list) + f" -o {PDF_OUTPUT_NAME} --from markdown+raw_tex --template {TEMPLATE_NAME} -V geometry:margin=1in -N --toc --toc-depth={TOC_DEPTH}  -V lang=fr-FR -V titlepage=true -V titlepage-color={TITLEPAGE_COLOR} -V titlepage-text-color={TITLEPAGE_TEXT_COLOR} -V titlepage-rule-color={TITLEPAGE_RULE_COLOR} -V titlepage-rule-height={TITLEPAGE_RULE_HEIGHT} -V titlepage-logo={TITLEPAGE_LOGO} -V logo-width={LOGO_WIDTH} -V titlepage-background={TITLEPAGE_BACKGROUND} -V page-background={PAGE_BACKGROUND} -V page-background-opacity={PAGE_BACKGROUND_OPACITY} -V toc-own-page=true -V book --top-level-division={TOP_LEVEL_DIVISION} -V classoption={CLASSOPTION} -V listings-no-page-break={LISTING_NO_PAGE_BREAK} --highlight-style={HIGHLIGHT_STYLE} --metadata=author:\"{METADATA_AUTHOR}\" --metadata=title:\"{METADATA_TITLE}\" --metadata=subject:\"{METADATA_SUBJECT}\" --metadata=subtitle:\"{METADATA_SUBTITLE}\" --metadata=date:\"{METADATA_DATE}\" --metadata=header-right:\"{HEADER_RIGHT}\" --metadata=header-center:\"{HEADER_CENTER}\" --metadata=header-left:\"{HEADER_LEFT}\" --metadata=footer-right:\"{FOOTER_RIGHT}\" --metadata=footer-center:\"{FOOTER_CENTER}\" --metadata=footer-left:\"{FOOTER_LEFT}\""
    os.system(cmd_line)
    return 0

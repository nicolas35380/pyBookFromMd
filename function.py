import subprocess
import os
import configparser

CONFIG_FILE = "config.ini"

# Load data from config file
def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, 'UTF-8')

    config_dict = {
        "md_requirement_files": config.get("general", "MD_REQUIREMENT_FILES"),
        "pdf_output_name": config.get("general", "PDF_OUTPUT_NAME"),
        "template_name": config.get("general", "TEMPLATE_NAME"),
        "toc_depth": config.getint("general", "TOC_DEPTH"),
        "top_level_division": config.get("general", "TOP_LEVEL_DIVISION"),
        "classoption": config.get("general", "CLASSOPTION"),
        "highlight_style": config.get("general", "HIGHLIGHT_STYLE"),
        "mermaid_support": config.getboolean("general", "MERMAID_SUPPORT"),
        "titlepage_logo": config.get("title-page", "TITLEPAGE_LOGO"),
        "logo_width": config.get("title-page", "LOGO_WIDTH"),
        "titlepage_color": config.get("title-page", "TITLEPAGE_COLOR"),
        "titlepage_text_color": config.get("title-page", "TITLEPAGE_TEXT_COLOR"),
        "titlepage_rule_color": config.get("title-page", "TITLEPAGE_RULE_COLOR"),
        "titlepage_rule_height": config.getint("title-page", "TITLEPAGE_RULE_HEIGHT"),
        "titlepage_background": config.get("title-page", "TITLEPAGE_BACKGROUND"),
        "page_background": config.get("any-page", "PAGE_BACKGROUND"),
        "page_background_opacity": config.get("any-page", "PAGE_BACKGROUND_OPACITY"),
        "metadata_author": config.get("metadata", "METADATA_AUTHOR"),
        "metadata_title": config.get("metadata", "METADATA_TITLE"),
        "metadata_subject": config.get("metadata", "METADATA_SUBJECT"),
        "metadata_subtitle": config.get("metadata", "METADATA_SUBTITLE"),
        "metadata_date": config.get("metadata", "METADATA_DATE"),
        "header_right": config.get("header-footer", "HEADER_RIGHT"),
        "header_center": config.get("header-footer", "HEADER_CENTER"),
        "header_left": config.get("header-footer", "HEADER_LEFT"),
        "footer_right": config.get("header-footer", "FOOTER_RIGHT"),
        "footer_center": config.get("header-footer", "FOOTER_CENTER"),
        "footer_left": config.get("header-footer", "FOOTER_LEFT"),
        "listing_no_page_break": config.get("listing", "LISTING_NO_PAGE_BREAK"),
    }
    return config_dict

# Open input file and read *.md
# return a list of *.md to append
def read_input_file(file):
    file_list = []
    with open(file, "r") as fp:
        file_list = fp.read().splitlines()
    return file_list

def mermaid_support():
    if mermaid_support:
        return " -F mermaid-filter.cmd"
    else:
        return ""

# Call to PANDOC and build PDF
# Return 0 for success, 1 for error (TODO)
def pdf_build(file_list, config):
    cmd_line = "pandoc " + subprocess.list2cmdline(file_list) + f" -o {config["pdf_output_name"]} --from markdown+raw_tex --template {config["template_name"]} -V geometry:margin=1in -N --toc --toc-depth={config["toc_depth"]} -V lang=fr-FR -V titlepage=true -V titlepage-color={config["titlepage_color"]} -V titlepage-text-color={config["titlepage_text_color"]} -V titlepage-rule-color={config["titlepage_rule_color"]} -V titlepage-rule-height={config["titlepage_rule_height"]} -V titlepage-logo={config["titlepage_logo"]} -V logo-width={config["logo_width"]} -V titlepage-background={config["titlepage_background"]} -V page-background={config["page_background"]} -V page-background-opacity={config["page_background_opacity"]} -V toc-own-page=true -V book --top-level-division={config["top_level_division"]} -V classoption={config["classoption"]} -V listings-no-page-break={config["listing_no_page_break"]} --highlight-style={config["highlight_style"]} --metadata=author:\"{config["metadata_author"]}\" --metadata=title:\"{config["metadata_title"]}\" --metadata=subject:\"{config["metadata_subject"]}\" --metadata=subtitle:\"{config["metadata_subtitle"]}\" --metadata=date:\"{config["metadata_date"]}\" --metadata=header-right:\"{config["header_right"]}\" --metadata=header-center:\"{config["header_center"]}\" --metadata=header-left:\"{config["header_left"]}\" --metadata=footer-right:\"{config["footer_right"]}\" --metadata=footer-center:\"{config["footer_center"]}\" --metadata=footer-left:\"{config["footer_left"]}\"" + mermaid_support()

    # print(cmd_line)
    os.system(cmd_line)
    return "Document " + config["pdf_output_name"] + " crée !"

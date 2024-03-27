from function import *

if __name__ == "__main__":

    config_dict = load_config()
    file = read_input_file(config_dict["md_requirement_files"])
    print(pdf_build(file, config_dict))
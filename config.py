import os
print(os.getcwd())
import yaml

class Config:
    def __init__(self, filename):
        with open("config.yml", 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)
            print(f"Config dictionary: {self.config}")

    def parse_yaml(self, yaml_string):
        in_quotes = False
        current_key = ""
        current_dict = {}
        result = {}

        for i, char in enumerate(yaml_string):
            if char == '"':
                in_quotes = not in_quotes

            if char == '{' and not in_quotes:
                current_dict = {}
                current_key = ""

            elif char == ':' and not in_quotes:
                current_key = current_key.strip()

            elif char == ',' and not in_quotes:
                result[current_key] = current_dict
                current_dict = {}
                current_key = ""

            elif char == '}' and not in_quotes:
                current_dict[current_key] = current_dict
                result[current_key] = current_dict
                current_dict = result
                current_key = ""

            elif char != ' ' and char != '\n':
                current_key += char
                if current_dict:
                    current_dict[current_key] = ""

        return result

    def get(self, section, key):
        if section in self.config and key in self.config.get(section, {}):
            return self.config[section][key]
        else:
            raise KeyError(f"Key '{key}' not found in section '{section}'")
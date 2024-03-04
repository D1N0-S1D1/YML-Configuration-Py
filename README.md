# YML Configuration in Python

A simple YAML configuration loader in Python.

## Installation

You can install the yml_configuration.p


## Usage
You should create file name_file.yml or run yml_configuration.py

You can use the Config class to load a YAML configuration file:

```
from yml_configuration import Config

config = Config('name_file.yml')

# Access a value from the configuration file
value = config.get('section', 'key')
```

## Configuration File
The configuration file should be a YAML file with the following structure:

```
section:
  key: value
```
For example:

```
Messages:
  Error: 'О ні! Ви не можете ввійти як адміністратор!'
```

You can create the configuration file manually, or use the 'create_config' function to create it:

```
from yml_configuration import Config

config = Config('name_file.yml')
config.create_config()
```

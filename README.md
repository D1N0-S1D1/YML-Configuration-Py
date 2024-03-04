# YML Configuration in Python

A simple YAML configuration loader in Python.

## Installation

You can install the package using `pip` with the following command:

```bash
pip install yml-configuration-py
```

Or, you can clone the GitHub repository and install the package with the following commands:

```
git clone https://github.com/D1N0-S1D1/YML-Configuration-Py.git
cd YML-Configuration-Py
pip install .
```

## Usage
You can use the Config class to load a YAML configuration file:

```
from yml_configuration import Config

config = Config('config.yml')

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

config = Config('config.yml')
config.create_config()
```

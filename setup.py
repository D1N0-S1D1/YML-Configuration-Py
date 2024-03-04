from setuptools import setup, find_packages

setup(
    name='yml-configuration-py',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'yml-config = yml_configuration:main',
        ],
    },
    author='D1N0-S1D1',
    author_email='dmytro__shevchuk@ukr.net',
    url='https://github.com/D1N0-S1D1/YML-Configuration-Py',
    license='MIT',
    description='A simple YAML configuration loader in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
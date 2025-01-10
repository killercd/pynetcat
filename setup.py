from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pynetcat",
    version="1.0.0",
    author="Renato Brescia",
    description="A python netcat implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,

    entry_points={
        "console_scripts": [
            "pynetcat=pynetcat.pynetcat:main",
        ],
    },
    python_requires=">=3.6",
)

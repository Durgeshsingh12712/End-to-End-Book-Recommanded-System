from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Edit Below variables as per ypur requirements

REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "DURGESH SINGH"
SRC_REPO = "bookrecommondedsystem"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Durgeshsingh12712/End-to-End-Book-Recommanded-System",
    author_email="durgeshsingh12712@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires = LIST_OF_REQUIREMENTS
)
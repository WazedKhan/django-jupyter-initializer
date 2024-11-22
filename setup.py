from setuptools import setup, find_packages
import pathlib

# Path to the directory containing README.md
current_dir = pathlib.Path(__file__).parent

# Read the long description from README.md
long_description = (current_dir / "README.md").read_text()

setup(
    name="django-jupyter-initializer",
    version="0.1.0",
    description="A utility to easily use Django in IDEs Jupyter Notebooks.",
    long_description=long_description,  # Use the README as the long description
    long_description_content_type="text/markdown",  # Markdown format
    author="Abdul Wajed Khan",
    author_email="wajed.abdul.khan@gmail.com",
    license="MIT",  # License type
    url="https://github.com/WazedKhan/django-jupyter-initializer",
    packages=find_packages(),
    install_requires=[],  # No dependencies other than Django
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
    ],
    keywords="django jupyter notebook development helper debugger",
)

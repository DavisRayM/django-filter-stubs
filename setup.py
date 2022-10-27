import os

from setuptools import setup
from pathlib import Path

name = "django-filter-stubs"


def find_stub_files(name):
    result = []
    for root, dirs, files in os.walk(name):
        for f in files:
            if f.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    f = os.path.join(sub_root, f)
                result.append(f)
    return result

long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    name="django-filter-stubs",
    version="0.1.2",
    description="PEP-484 stubs for django-filter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/DavisRayM/django-filter-stubs",
    author="Davis Raymond Muro",
    author_email="davisraymondmuro@outlook.com",
    packages=['django_filters-stubs'],
    package_data={"django_filters-stubs": find_stub_files('django_filters-stubs')},
    install_requires=[
        "mypy>=0.750",
        "django-stubs>=1.3.0",
        "djangorestframework-stubs>=0.4.0",
        "typing-extensions>=3.7.4",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)

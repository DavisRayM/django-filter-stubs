import os

from setuptools import setup

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


setup(
    name="django-filter-stubs",
    version="0.1.1",
    description="PEP-484 stubs for django-filter",
    license="MIT",
    url="https://github.com/DavisRayM/django-filter-stubs",
    author="Davis Raymond Muro",
    author_email="davisraymondmuro@outlook.com",
    packages=['django_filters-stubs'],
    package_data={"django_filters-stubs": find_stub_files('django_filters-stubs')},
    install_requires=[
        "mypy>=0.750",
        "django-stubs>=1.3.0",
        "djangorestframework-stubs>=0.4.0" "typing-extensions>=3.7.4",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)

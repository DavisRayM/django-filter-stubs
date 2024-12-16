import os
from pathlib import Path

from setuptools import setup

name = "django-filter-stubs"


def find_stub_files(name):
    result = []
    for root, _, files in os.walk(name):
        for f in files:
            if f.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    f = os.path.join(sub_root, f)
                result.append(f)
    return result


long_description = (Path(__file__).parent / "README.md").read_text()


setup(
    packages=["django_filters-stubs"],
    package_data={"django_filters-stubs": find_stub_files("django_filters-stubs")},
)

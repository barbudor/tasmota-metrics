import os.path

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def get_long_description():
    with open("README.md", "r") as f:
        text = f.read()
    return text


setup(
    name="tasmota-metrics",
    version=get_version("tasmota_metrics/__init__.py"),
    author="Espressif Systems",
    author_email="",
    description="Firmware size analysis for ESP-IDF",
    long_description_content_type="text/markdown",
    long_description=get_long_description(),
    url="https://github.com/jason2866/tasmota-metrics",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["pyyaml"],
    extras_require={
        "dev": [
            "pre-commit",
            "coverage",
            "jsonschema",
        ],
    },
    keywords=["espressif", "embedded", "project", "size"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Topic :: Software Development :: Embedded Systems",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ],
    include_package_data=True,
)

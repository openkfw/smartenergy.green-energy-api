"""Package setup"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="electricity_maps_api",
    version="0.2.0",
    author="",
    author_email="",
    description="A python library to access the Electricity Maps API",
    license="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: TBD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    provides=["electricity_maps_api"],
    install_requires=["requests"],
    setup_requires=["wheel"],
)

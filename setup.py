from setuptools import setup, find_packages

setup(
    name="MediaSurfer",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "bs4",
        "cloudscraper"#
    ],
    description="MediaSurfer is a powerful Python library that allows you to easily download media from multiple social platforms.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="ARIFI",
    url="https://github.com/arifiios/MediaSurfer",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

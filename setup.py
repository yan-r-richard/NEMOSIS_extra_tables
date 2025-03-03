import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nemosis",
    version="3.5.1",
    author="Nicholas Gorman, Abhijith Prakash",
    author_email="n.gorman305@gmail.com",
    description="A tool for accessing AEMO data.",
    long_description="A tool for accessing AEMO data.",
    long_description_content_type="text/markdown",
    url="https://github.com/yan-r-richard/NEMOSIS_extra_tables",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "joblib",
        "pyarrow",
        "feather-format",
        "pandas",
        "xlrd",
        "beautifulsoup4",
        "openpyxl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)

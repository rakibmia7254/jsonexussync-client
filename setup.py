from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    l_description = fh.read()


setup(
    name="jsonexussync-client",
    version="1.0.1",
    packages=find_packages(),
    long_description=l_description,
    long_description_content_type="text/markdown",
    description="client library of client JSONexusSync",
    author="Rakib Hossain",
    author_email="rakib4ggp@gmail.com",
    license="MIT",
    keywords="remote-database",
    url="https://github.com/rakibma7254/jsonexussync-client",
    install_requires=['websockets'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)


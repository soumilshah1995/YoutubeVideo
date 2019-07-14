from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Youtube-Video",
    version="1.0.1",
    description="A Python package to get all Youtube Videos and save Excel or Json",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/YoutubeVideo",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["YTD_Master"],
    include_package_data=True,
    install_requires=["google-api-python-client==1.7.8","pandas>=0.24.0"]
    )
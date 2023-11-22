import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="log_utils",
    version="0.0.1",
    author="Daniel Sturdivant",
    author_email="sturdivant20@gmail.com",
    description="simple logging utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gavlab-radiance/log_utils",
    # install_requires=["python-dateutil>2.8.1"],
    packages=setuptools.find_packages(),
)
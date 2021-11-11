import setuptools

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except UnicodeDecodeError:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

with open("logs/const/const.py", encoding="utf-8") as f:
    exec(f.read())

setuptools.setup(
    name="aioowm",
    version=locals()["__version__"],
    author=locals()["__author__"],
    description="Library for sending color logs Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/vladislavkovalskyi/logs",
    packages=setuptools.find_packages(),
    author_email="v.darknesssb@gmail.com",
    classifiers=[
        "Operating System :: OS Independent",
    ],
    install_requires=[]
)

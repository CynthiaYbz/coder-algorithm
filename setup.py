from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        README = f.read()
    return README


with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("requirements-test.txt") as f:
    test_required = f.read().splitlines()

setup(
    name="coder-python",
    version="1.0.0",
    description="I am a coder, I learn python now , so I make my first repository name is coder-python.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/CynthiaYbz/coder-python",
    author="Cynthia",
    license="Apache License",
    classifiers=[
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=required,
    extras_require={"full": required,
                    "test": test_required + required},
)
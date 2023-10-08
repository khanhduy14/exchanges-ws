import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="exchanges-websocket",
    version="0.0.1",

    description="Centralize websocket from various exchanges",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

    install_requires=[
        "websockets==11.0.3",
        "pytest==7.4.2",
        "kafka-python",
        "configparser"
    ],

    python_requires=">=3.10",

    classifiers=[
        "Development Status :: 1 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10"

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
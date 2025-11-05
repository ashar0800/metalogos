from setuptools import setup, find_packages

setup(
    name="metalogos",
    version="0.1.0",
    author="Ashar Nasir",
    author_email="your_email@example.com",
    description="Where logic meets longing — a library for reflective computation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/razdaan/metalogos",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
)

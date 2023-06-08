from setuptools import setup

setup(
    name="henhoe2vec",
    version="0.0.1",
    description="Implementation of the HeNHoE-2vec algorithm by Valentini et al. (2021).",
    py_modules=["henhoe2vec"],
    package_dir={"": "src"},
    url="https://github.com/Bertr0/HeNHoE-2vec",
    author="Robert Giesler",
    author_email="robert.giesler@rwth-aachen.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

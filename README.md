# HeNHoE-2vec
A Python implementation of the HeNHoE-2vec algorithm by [Valentini et al.](https://arxiv.org/abs/2101.01425) for the embedding of networks with heterogeneous nodes and homogeneous edges (HeNHoE).

_Note_: HeNHoE networks are analogous to multilayer networks: in HeNHoE networks, each node has a distinct node type, and in multilayer networks, each node belongs to a distinct layer. The terms `type` and `layer` may therefore be regarded synonymous. Throughout the code and for the remainder of this documentation, we will use the terms `multilayer network` and `layer` as opposed to `HeNHoE network` and `type`.

## Installation
Install the package from PyPI by running the following command:
```
pip install henhoe2vec
```

Alternatively, clone this repository by running
```
git clone git@github.com:Bertr0/HeNHoE-2vec.git
```

and then install the package by running `pip install .` from the root of the repository.

## Usage
This package may be used as a Python script or as a package, allowing its modules to be imported by other Python projects. Both forms of use make it easy to run HeNHoE-2vec on multilayer networks.

### As a Package
After installing the package using `pip`, its modules may be imported using
```python
import henhoe2vec
```

The many individual steps of HeNHoE-2vec are accumulated in a single `run()` method in the `henhoe2vec.henhoe2vec` module. HeNHoE-2vec can be run from start to finish as follows:
```python
import henho2vec as hh2v

hh2v.henhoe2vec.run(input_csv, output_dir)
```

`input_csv` is the path to the multilayer edge list of the network to be embedded (csv file with tab delimiter, no header, no index). `output_dir` is the path to the output directory where the embedding files will be saved.

### As a Python Script
To run HeNHoE-2vec as a script, clone this repositiory by running
```
git clone git@github.com:Bertr0/HeNHoE-2vec.git
```

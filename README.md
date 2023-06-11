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

`input_csv` is the path to the multilayer edge list of the network to be embedded (csv file with tab delimiter, no header, no index). `output_dir` is the path to the output directory where the embedding files will be saved. The `run()` method takes a bunch of other optional parameters which can be used to configure HeNHoE-2vec. A comprehensive overview of parameters can be found in the code documentation.

### As a Python Script
To run HeNHoE-2vec as a script, clone this repositiory using
```
git clone git@github.com:Bertr0/HeNHoE-2vec.git
```
, install the requirements found in `requirements.txt` and run the following command from the root of the repository:
```
python3 -m src.henhoe2vec.henhoe2vec --input <input_path> --output_dir <output_dir_path>
```

This will generate node embedddings for the nodes of the network specified by the mutlilayer edge list saved at `<input_path>` and saves the embedding files in `<output_dir>`.

Run `python3 -m src.henhoe2vec.henhoe2vec --help` from the root of the repository to show an overview of all arguments taken by the script. The following table also shows an overview of all arguments:

#### Script Arguments
| Argument | Type | Description | Default Value |
| -------- | ---- | ----------- | ------------- |
| `--input` | str | Path to the multilayer edge list of the network to be embedded (.csv file with tab delimiter, no header, no index). | - |
| `--is-directed` | store_true | Pass this argument if the network is directed. | - |
| `--edges-are-distances` | store_true | Pass this argument if edge weights indicate distance between nodes (opposed to weight/similarity). | - |
| `--output_dir` | str | Path of the output directory where the embedding files will be saved. | - |
| `--dimensions` | int | The dimensionality of the embeddings. | 128 |
| `--walk-length` | int | Length of each random walk. | 20 |
| `--num-walks` | int | Number of randwom walks to simulate for each node. | 10 |
| `--p` | float | Return parameter `p` from the node2vec algorithm. | 1.0 |
| `--q` | float | In-out parameter `q` from the node2vec algoritym. | 0.5 |
| `--s` | float | Default switching parameter for layer pairs which are not specified in the `--s-dict` argument. | 1.0 |
| `--s-dict` | list | Switching parameters for specific layer pairs in a dict-like manner. Pass the names of layer pairs followed by their switching parameters, separated by whitespaces. E.g., if the switching parameter from `layer1` to `layer2` is `0.5` and the switching parameter from `layer2` to `layer1` is `0.7`, you would pass `layer1 layer2 0.5 layer2 layer1 0.7`. Note that layer pairs are directed. For all layer pairs which are not specified here, the default parameter `--s` is adopted. | empty list |
| `--window-size` | int | Context size for the word2vec optimization. | 10 |
| `--epochs` | int | Number of epochs in SGD. | 1 |
| `--workers` | int | Number of parallel workers (threads). | 8 |

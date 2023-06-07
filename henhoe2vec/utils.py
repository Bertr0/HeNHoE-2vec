import networkx as nx
import time
import pandas as pd
from pathlib import Path


# --------------------------------------------------------------------------------------
# PARSING AND CONVERSION FOR MULTILAYER NETWORKS
# --------------------------------------------------------------------------------------
def parse_multilayer_edgelist(multiedgelist, directed):
    """
    Convert a multilayer edge list into a NetworkX Graph.

    Parameters
    ----------
    multiedgelist : str
        Path to the multilayer edge list (csv file with tab delimiter, no header, no
        index) to be converted. Consists of the columns 'source', 'source_layer',
        'target', 'target_layer', 'weight'.
    directed : bool
        Whether the network is directed or not.

    Returns
    -------
    NetworkX (Di)Graph
        Multilayer network parsed from the passed in edge list. Nodes are tuples of the
        form ('n','l') where 'n' is the name of the node and 'l' is the layer it belongs
        to. Every node additionally has an attribute 'layer' which denotes its layer.
        Edges have an attribute 'weight'.
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    with open(multiedgelist) as IN:
        for line in IN:
            parts = line.strip().split()
            if len(parts) == 5:
                source, source_layer, target, target_layer, weight = parts
            elif len(parts) == 4:
                source, source_layer, target, target_layer = parts
                weight = 1
            else:
                raise ValueError(
                    f"[ERROR] mutliedgelist has too many columns: {len(parts)}. The"
                    f" columns should be 'source', 'source_layer', 'target',"
                    f" 'target_layer', 'weight'."
                )

            G.add_node((source, source_layer), layer=source_layer)
            G.add_node((target, target_layer), layer=target_layer)
            G.add_edge(
                (source, source_layer), (target, target_layer), weight=float(weight)
            )

    return G


# --------------------------------------------------------------------------------------
# OUTPUT
# --------------------------------------------------------------------------------------
def timed_invoke(action_desc, method):
    """
    Invoke a method with timing.

    Parameters
    ----------
    action_desc : str
        The string describing the method action.
    method : function
        The method to invoke.

    Returns
    -------
    object
        The return object of the method.
    """
    print(f"Started {action_desc}...")
    start = time.time()
    try:
        output = method()
        print(f"Finished {action_desc} in {int(time.time() - start)} seconds")
        return output
    except Exception:
        print(f"Exception while {action_desc} after {int(time.time() - start)} seconds")
        raise


def emb_to_pandas(emb_file):
    """
    Convert an embedding file, as output from a trained word2vec model, to a pandas
    DataFrame.

    Parameters
    ----------
    emb_file : str
        Absolute path of the word2vec embedding file.

    Returns
    -------
    pandas DataFrame
        word2vec embedding as a dataframe.
    """
    embedding = pd.read_csv(
        emb_file, delim_whitespace=True, skiprows=1, header=None, index_col=0
    )
    embedding.sort_index(inplace=True)

    return embedding


def clean_output_directory(dir_path):
    """
    Check if output directory exists, otherwise created it.

    Parameters
    ----------
    dir_path : str
        Path of the output directory.

    Returns
    -------
    str
        Absolute path of the output directory.
    """
    directory = Path(dir_path)
    if directory.is_dir():
        return str(directory)
    else:
        directory.mkdir()
        print(f"Created output directory {directory}.")
        return str(directory)

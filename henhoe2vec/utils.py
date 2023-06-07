import networkx as nx
import time


# --------------------------------------------------------------------------------------
# PARSING AND CONVERSION FOR MULTILAYER GRAPHS
# --------------------------------------------------------------------------------------
def parse_multilayer_edgelist(multiedgelist, directed):
    """
    Converts a multilayer edge list into a NetworkX Graph.

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
            G.add_edge((source, source_layer), (target, target_layer), weight=weight)

    return G


# --------------------------------------------------------------------------------------
# OUTPUT
# --------------------------------------------------------------------------------------
def timed_invoke(action_desc, method):
    """
    Invokes a method with timing.

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

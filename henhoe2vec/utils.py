import py3plex.core.multinet as multinet

# -------------------------------------------------------------------------------
# PARSING AND CONVERSION FOR MULTILAYER GRAPHS
# -------------------------------------------------------------------------------
def parse_multilayer_edgelist(multiedgelist, directed):
    """
    Converts a multilayer edge list into a py3plex multinet.

    Parameters
    ----------
    multiedgelist : str
        Path to the multilayer edge list (csv file with tab delimiter, no header, no index)
        to be converted. Consists of the columns source, source_layer, target, target_layer,
        weight.
    directed : bool
        Whether the network is directed or not.

    Returns
    -------
    py3plex multinet
        Multilayer network parsed from the passed in edge list.
    """
    return multinet.multi_layer_network().load_network(
        multiedgelist, input_type="multiedgelist", directed=directed
    )

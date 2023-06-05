import py3plex.core.multinet as multinet
import time

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


# -------------------------------------------------------------------------------
# OUTPUT
# -------------------------------------------------------------------------------
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
    print('Started {}...'.format(action_desc))
    start = time.time()
    try:
        output = method()
        print('Finished {} in {} seconds'.format(action_desc, int(time.time() - start)))
        return output
    except Exception:
        print('Exception while {} after {} seconds'.format(action_desc, int(time.time() - start)))
        raise
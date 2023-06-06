import numpy as np
import py3plex

class HenHoe2vec():
    """
    A class to generate HeNHoE-2vec random walks over a heterogeneous-node
    homogeneous-edge network.

    Attributes
    ----------
    henhoe_network : py3plex multinet
        Heterogeneous-node homogeneous-edge network.
    is_directed : bool
        Whether the network is directed or not.
    p : float
        The return parameter `p` from the node2vec algorithm.
    q : float
        The in-out parameter `q` from the node2vec algorithm.
    s : dict
        The type-switching parameter(s) of the HeNHoE-2vec algorithm.
    transition_probs_nodes : dict
        Transition probability distribution to neighbors of each node based only on edge
        weights and switching parameters.
    transition_probs_edges : dict
        Transition probability distribution to neighbors of each node based on edge
        weights, p, q, and switching parameters.
    """
    def __init__(self, henhoe_network, is_directed, p, q, s):
        """
        Constructor for the HenHoe2vec class.

        Parameters
        ----------
        henhoe_network : py3plex multinet
            Heterogeneous-node homogeneous-edge network.
        is_directed : bool
            Whether the network is directed or not.
        p : float
            The return parameter `p` from the node2vec algorithm.
        q : float
            The in-out parameter `q` from the node2vec algorithm.
        s : float or dict
            The type-switching parameter(s) of the HeNHoE-2vec algorithm. There are two
            modes:
            Simple switching: If the probability to switch between layers should be the
            same for all pairs of layers, passing a single float suffices.
            Versus specific switching: We might want to have different probabilities for
            switching between specific layers. In this case, we can pass a dict of the
            form {("layer1","layer2") : 0.5, ("layer2","layer1") : 0.2, "default" : 1}.
            Note that the layer pairs are directed, i.e., the switching parameter from
            layer1 to layer2 may be different than the switching parameter from layer2
            to layer1. The "default" switching parameter is used for layer pairs which
            don't have an explicit entry in the dict.
            The switching modes "multiple switching" and "special node switching" (which
            we don't explicitly implement here) are special cases of "versus specific
            switching".

        Returns
        -------
        HenHoe2vec
            Constructed HenHoe2vec object.
        """
        self.N = henhoe_network
        self.is_directed = is_directed
        self.p = p   # Return parameter
        self.q = q   # In-out parameter

        # Transition probability distribution to neighbors of each node based only on
        # edge weights and switching parameters. Only used for first step of each walk
        # where there is no previous node.
        # Form: {node : (J, q)}
        self.transition_probs_nodes = {}
        # Transition probability distribution to neighbors of each node based on edge
        # weights, p, q, and switching parameters. Used for all other steps of the walk.
        # Form: {(node1, node2) : (J, q)}
        self.transition_probs_edges = {}
        
        if type(s) in [float, int]:
            self.s = {"default" : s}
        elif type(s) == dict:
            self.s = s
        else:
            raise TypeError(
                f"[ERROR]: Invalid type for argument s. Should be float or dict but"
                f" is {type(s)}."
            )
        

    def henhoe2vec_walk(self, walk_length, start_node):
        """
        Simulate a random walk starting from `start_node`.

        Parameters
        ----------
        walk_length : int
            Length of the random walk.
        start_node : NetworkX node
            Starting node of the random walk.

        Returns
        -------
        list of NetworkX nodes
            Random walk of length `walk_length` starting at `start_node`.
        """

    
    def preprocess_transition_probs(self):
        """
        Preprocessing of transition probabilities for guiding the random walks.
        """
        N = self.N
        is_directed = self.is_directed

        transition_probs_nodes = {}
        transition_probs_edges = {}

        for 
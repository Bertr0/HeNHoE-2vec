import argparse
import time
from utils import parse_multilayer_edgelist
import henhoe2vec
import embeddings


def parse_args():
    """
    Parse arguments for HeNHoE-2vec.
    """
    parser = argparse.ArgumentParser(description="Run HeNHoE-2vec.")

    parser.add_argument(
        "--input",
        type=str,
        help="Path to the multilayer edge list of the network to be embedded.",
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Path of the output directory where the embedding files shall be saved.",
    )

    parser.add_argument(
        "--dimensions",
        type=int,
        default=128,
        help="The dimensionality of the embeddings.",
    )

    parser.add_argument(
        "--walk-length", type=int, default=20, help="Length of each random walk."
    )

    parser.add_argument(
        "--num-walks",
        type=int,
        default=10,
        help="Number of random walks to simulate for each node.",
    )

    parser.add_argument(
        "--window-size", type=int, default=10, help="Context size for optimization."
    )

    parser.add_argument(
        "--p",
        type=float,
        default=1,
        help="Return parameter p from the node2vec algorithm.",
    )

    parser.add_argument(
        "--q",
        type=float,
        default=0.5,
        help="In-out parameter q from the node2vec algorithm.",
    )

    parser.add_argument(
        "--s",
        nargs="*",
        default=[],
        help=(
            "The type-switching parameter(s) of the HeNHoE-2vec algorithm. If the"
            " probability to switch between layers should be the same for all pairs"
            " of layers, pass a single float. We might want to have"
            " different probabilities for switching between specific layers. In"
            " this case, pass the names of layer pairs followed by their switching"
            " parameters, sperarated by whitespaces, e.g., 'layer1 layer2 0.5"
            " layer2 layer1 0.7'. Note that layer pairs are directed."
        ),
    )

    parser.add_argument(
        "--default-s",
        type=float,
        default=None,
        help=(
            "Default switching parameter for layer pairs which are not specified"
            " in the --s argument."
        ),
    )

    parser.add_argument("--epochs", default=1, type=int, help="Number of epochs in SGD")

    parser.add_argument(
        "--workers", type=int, default=8, help="Number of parallel workers (threads)."
    )

    parser.add_argument(
        "--is-directed",
        action="store_true",
        help="Pass this argument if the network is directed.",
    )

    return parser.parse_args()


def parse_switching_param(s, default_s):
    """
    Parse the switching arguments s and default-s passed into the script.

    Parameters
    ----------
    s : list or None
            Argument s passed into the script.
    default-s : float
            Argument default-s passed into the script.

    Returns
    -------
    float or dict
            s and default-s parsed into a float or dict.
    """
    # No values passed for s
    if not s:
        return default_s
    # Single value passed for s
    if len(s) == 1:
        if default_s:
            print(f"[WARNING] Both s and default-s were set. Using s: {s[0]}")
        return float(s[0])
    else:
        switching_dict = {}
        while len(s) > 0:
            triple = s[:3]
            s = s[3:]
            try:
                switching_dict[(triple[0], triple[1])] = float(triple[2])
            except:
                raise ValueError(
                    f"[ERROR] Argument --s has the wrong form. Should be a single float"
                    f" or consist of 'layer layer s' triples, e.g., 'layer1 layer2 0.5"
                    f" layer2 layer1 0.7'."
                )
        return switching_dict


if __name__ == "__main__":
    args = parse_args()
    s = parse_switching_param(args.s, args.default_s)

    N_nx = parse_multilayer_edgelist(args.input, args.is_directed)
    N = henhoe2vec.HenHoe2vec(N_nx, args.is_directed, args.p, args.q, s)
    N.preprocess_transition_probs()
    walks = N.simulate_walks(args.num_walks, args.walk_length)
    embeddings.generate_embeddings(walks, args.output)

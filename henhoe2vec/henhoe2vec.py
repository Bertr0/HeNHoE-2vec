from gensim.models import word2vec as w2v

from utils import emb_to_pandas, clean_output_directory


def generate_embeddings(
    walks, output_dir, dimensions=128, window_size=10, epochs=1, workers=8
):
    """
    Learns the embeddings of the nodes by optimizing the Skipgram objective using SGD.
    Saves embeddings to `output_dir` in word2vec and csv format.

    Parameters
    ----------
    walks : list of list of 2-tuples of strs
        The list of random walks generated over the HeNHoE network.
    out_dir : str
        Path to the output directory where the embedding files shall be saved, e.g.,
        "project/output/".
    dimensions : int
        The dimensionality of the embeddings. Default is 128.
    window_size : int
        Context size for optimization. Default is 10.
    epochs : int
        Number of epochs in SGD. Default is 1.
    workers : int
        Number of parallel workers (threads). Default is 8.
    """
    # Generate embeddings
    walks = [map(str, walk) for walk in walks]
    model = w2v.Word2Vec(
        walks,
        size=dimensions,
        window=window_size,
        epochs=epochs,
        min_count=0,
        sg=1,
        workers=workers,
    )

    # Save embeddings
    output_dir = clean_output_directory(output_dir)
    output_emb = output_dir.join("henhoe2vec_results.emb")
    model.save_word2vec_format(output_emb)

    output_csv = output_dir.join("henhoe2vec_results.csv")
    embedding_df = emb_to_pandas(output_emb)
    embedding_df.to_csv(output_csv, sep="\t", header=False)

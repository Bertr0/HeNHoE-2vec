from pathlib import Path


def save_test_edgelist(edgelist_df, path, sep, header):
    """
    Save a test edge list passed in as DataFrame as a .edg file (csv) in path.

    Parameters
    ----------
    edgelist_df : pandas.DataFrame object
        Test edge list to be saved as a pandas DataFrame.
    path : pathlib.Path object
        Directory where the edge list will be saved.
    sep : str
        Delimiter of the output .csv file.
    header : bool
        Whether the output .csv file has a header.

    Returns
    -------
    pathlib.Path object
        Save location of the test edge list.
    """
    save_path = Path.joinpath(path, "test_edgelist.edg")
    edgelist_df.loc[
        :, ["source", "source_layer", "target", "target_layer", "weight"]
    ].to_csv(save_path, sep=sep, index=False, header=header)

    return save_path

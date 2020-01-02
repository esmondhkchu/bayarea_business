import numpy as np

def count_n_sort(in_arr, top_n=None, descending=True):
    """ count an array and return a sorted dictionary
    arg: in_arr (tuple/list/array/Series) - the input array
         top_n (int) - return the top n values, optional, default is None, return everything
         descending (boolean) - order of sorted dictionary, optional, default is True
    return: sorted_dict (dict) - a dictionary with the format {val:count}
    """
    val, count = np.unique(in_arr, return_counts=True)

    if top_n == None:
        top_n = len(in_arr)
    else:
        top_n = top_n

    if descending:
        sorted_idx = np.argsort(count)[::-1]
        sorted_dict = {i:j for i,j in zip(val[sorted_idx][:top_n], count[sorted_idx][:top_n])}
    else:
        sorted_idx = np.argsort(count)
        sorted_dict = {i:j for i,j in zip(val[sorted_idx][:top_n], count[sorted_idx][:top_n])}

    return sorted_dict

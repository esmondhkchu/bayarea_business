import requests
import json

from tqdm import tqdm_notebook as tqdm
import pandas as pd

def get_businesses_request(api_key, term, location, offset, radius=40000):
    """ make a request to get businesses information based on location and term

    Parameters: api_key (str) - your yelp fusion api key
                term (str) - search term
                location (str) - businesses location
                offset (int) - search research page, eg, 50 -> get first 0-50 pages
                radius (int) - in meters, a suggested search radius, optional, default is 40,000

    Returns: parsed (dict) - the request information
    """
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':term, 'location':location, 'limit':50, 'offset':offset, 'radius':radius}

    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)

    return parsed

def get_all_businesses_request(api_key, term, location, radius=40000):
    """ make a request to get all businesses information based on location and term

    Parameters: api_key (str) - your yelp fusion api key
                term (str) - search term
                location (str) - businesses location
                radius (int) - in meters, a suggested search radius, optional, default is 40,000

    Returns: all_businesses (list) - a list of all businesses information, each business in a dict
    """
    first_query = get_businesses_request(api_key, term, location, offset=0, radius=radius)
    total = first_query['total']

    if total >= 1000:
        other_query = [get_businesses_request(api_key, term, location, offset=i, radius=radius) for i in range(50, 1000, 50)]
        other_businesses = [i['businesses'] for i in other_query]
    else:
        other_query = [get_businesses_request(api_key, term, location, offset=i, radius=radius) for i in range(50, total, 50)]
        other_businesses = [i['businesses'] for i in other_query]

    all_businesses = first_query['businesses'] + [j for i in other_businesses for j in i]

    return all_businesses

def get_business_reviews(api_key, id_):
    """ get the reviews information of a business

    Parameters: api_key (str) - your yelp fusion api key
                id_ (str) - a yelp business id

    Parameters: reviews (list) - a list of reviews information
    """
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(id_)
    req = requests.get(url, headers=headers)
    parsed = json.loads(req.text)
    reviews = parsed['reviews']

    return reviews

def get_businesses_reviews(api_key, id_list, verbose=True):
    """ get reviews of a list of businesses

    Parameters: api_key (str) - your yelp fusion api key
                id_list (tuple/list/array like) - a list of yelp id for their reviews
                verbose (boolean) - print extraction message or not
                                    optional, default is True

    Returns: all_reviews (dict) - a dictionary in the format {id:list of business reviews}
    """
    all_reviews = {}
    retry_id = []

    for i in tqdm(id_list):
        try:
            all_reviews[i] = get_business_reviews(api_key, i)
        except:
            if verbose:
                print('Failed to extract: {}; will retry later'.format(i))
            retry_id.append(i)

    if retry_id:
        for i in retry_id:
            try:
                all_reviews[i] = get_business_reviews(api_key, i)
                if verbose:
                    print('Retrying: {}; Status: Success'.format(i))
            except:
                if verbose:
                    print('Failed to extract: {}'.format(i))

    return all_reviews

def one_dict_to_df(id_, in_list):
    """ transform a dictionary from get_businesses_reviews() to a pd.DataFrame
        for a single id, use it as a component for a macro function

    Parameters: id_ (str) - a string of single business id_
                in_list (list) - a list of review information, within the list, each review is a dict

    Returns: df (DataFrame) - a dataframe which users' information are dropped
    """
    business_id = [id_]*len(in_list)
    id_df = pd.DataFrame({'business_id':business_id})
    main_df = pd.DataFrame(in_list).drop(columns='user')
    df = pd.concat([id_df, main_df], axis=1)

    return df

def dict_to_df(in_dict):
    """ transform a dictionary from get_businesses_reviews() to a pd.DataFrame

    Parameters: in_dict (dict) - a dict from get_businesses_reviews()

    Returns: df (DataFrame) - a dataframe with all reviews from all businesses
    """
    all_ids = list(in_dict)
    all_dfs = [one_dict_to_df(i, in_dict[i]) for i in all_ids]
    df = pd.concat(all_dfs, axis=0)

    return df

# ------------------------------------------------------------------ #
class YelpCalls:
    """ extract businesses information in a given location

    >>> query = YelpCalls(api_key, term, location)
    >>> info_df = query.get_all_businesses_info_df()
    # initiate all reviews
    >>> query.get_all_reviews(return_=False, verbose=True)
    >>> reviews_df = query.get_all_reviews_df()
    # save to .json
    >>> query.save_all_businesses_info(file_name)
    >>> query.save_all_reviews(file_name)
    """
    def __init__(self, api_key, term, location, radius=40000):
        self.api_key = api_key
        self.term = term
        self.location = location
        self.radius = radius

        self.all_businesses_info = get_all_businesses_request(self.api_key, self.term, self.location, self.radius)
        self.all_businesses_ids = [i['id'] for i in self.all_businesses_info]

    def get_all_reviews(self, return_=False, verbose=True):
        self.reviews_dict = get_businesses_reviews(self.api_key, self.all_businesses_ids, verbose)
        if return_:
            return self.reviews_dict

    # --save to .json-- #
    def save_all_businesses_info(self, file_name):
        """ save self.all_businesses_info as a .json file
        """
        save_dict = {'location':self.location,
                     'term':self.term,
                     'radius':self.radius,
                     'businesses':self.all_businesses_info}

        with open(file_name, 'w') as json_file:
            json.dump(save_dict, json_file)

    def save_all_reviews(self, file_name):
        """ save self.review_dict as a .json file
        """
        save_dict = {'location':self.location,
             'term':self.term,
             'radius':self.radius,
             'reviews':self.reviews_dict}

        with open(file_name, 'w') as json_file:
            json.dump(save_dict, json_file)

    # --to df-- #
    def get_all_businesses_info_df(self):
        return pd.DataFrame(self.all_businesses_info)

    def get_all_reviews_df(self):
        return dict_to_df(self.reviews_dict)

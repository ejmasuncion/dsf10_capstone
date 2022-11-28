import pandas as pd

def extract_nested_dict(data, col):
    """extract column with nested dictionary structure into a dataframe.
    Used to format raw scraped review data 

    Args:
        data (dataframe): dataframe containing the column with the nested dictionary
        col (str): column name of the nested dictionary

    Return:
        a dataframe with dictionary keys as columns and url
    """
    df = []
    for i in range(len(data)):
        url_data = data['url'][i]
        nested_dict = data[col][i]
        for key in nested_dict:
            dict = nested_dict[str(key)]
            temp  = pd.DataFrame.from_dict(dict, orient = 'index').reset_index()
            temp.rename(columns = {0:'value'}, inplace = True)
            temp = temp.set_index('index').T.reset_index(drop=True)
            temp = temp.replace(r'\n',' ', regex=True) 
            temp = temp.replace(r'·',' ', regex=True) 
            temp['url'] = url_data
            df.append(temp)

    return(pd.concat(df))


def extract_dict(data, col):
    """extract dictionary column into a dataframe

    Args:
        data (dataframe): dataframe containing the column with the dictionary
        col (str): column name of the dictionary
    """
    df = []
    for i in range(len(data['hotel_name_'])):
        hotel_name = data['hotel_name_'][i]
        sub_data = data[col][i]
        temp  = pd.DataFrame.from_dict(sub_data, orient = 'index').reset_index()
        temp['hotel_name_'] = hotel_name
        temp.rename(columns = {0:'value', 'index':'category'}, inplace = True)
        df.append(temp)
    return(pd.concat(df))


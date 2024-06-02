"""
This file contains utility functions that are used in the project.
"""

import pandas as pd
import logging
import yaml


def read_yaml(file_path):
    """
    Read yaml file and return the content

    Parameters
    ----------
    file_path : str
        The path to the yaml file

    Returns
    -------
    dict
        The content of the yaml file
    """

    logging.info("Reading config file")
    with open(file_path, "r") as file:
        config_data = yaml.safe_load(file)
    return config_data


def read_csv(file_path):
    """
    Read csv file and return a pandas dataframe

    Parameters
    ----------
    file_path : str
        The path to the csv file

    Returns
    -------
    pandas.DataFrame
        The data from the csv file
    """

    logging.info(f"Reading data from {file_path}")
    data = pd.read_csv(file_path, engine="python", encoding="utf-8")
    return data
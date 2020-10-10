from bigquery import AustinCrime
from unittest import mock
import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


test_df_clean_data = pd.DataFrame({'x1':[0,1,2,3,4],'location':[2,3,4,np.nan,6]})
def test_clean_data():
    """Testing which index will be drop from dataframe"""
    original_index = set(test_df_clean_data.index)
    clean_df = AustinCrime.clean_data(test_df_clean_data)
    clean_index = set(clean_df.index)
    assert (set(test_df_clean_data.index)- set(clean_df.index)) == {3}
    
test_df_clean_data1 = pd.DataFrame({'x1':[0,1,2,3,4],'location':[2,3,4,0,6]})
def test_clean_data_no_null():
    """Testinf if df before and after clean_data is the same"""
    clean_df = AustinCrime.clean_data(test_df_clean_data1)
    
    assert test_df_clean_data1.equals(clean_df)
    
test_df_clean_data2 = pd.DataFrame({'x1':[0,1,2,3,4],'loc':[2,3,np.nan,0,6]})
def test_clean_data_no_column():
    """Testing df without column location"""
    with pytest.raises(AttributeError):
        clean_df = AustinCrime.clean_data(test_df_clean_data2)


def test_popular_crime():
    """
    Read df form pickle
    In mock.patch output of read_data_from_big_query is set
    Test type of object
    """
    test_df = pd.read_pickle('test_df.pickle')
    with mock.patch('bigquery.AustinCrime.read_data_from_big_query', return_value=test_df):
        obj = AustinCrime('SELECT test')
        obj.popular_crime()
        plot_test = plt.gca()
        assert isinstance(plot_test,plt.Axes)

    

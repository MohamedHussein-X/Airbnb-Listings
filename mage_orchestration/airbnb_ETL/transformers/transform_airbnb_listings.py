from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.FILTER

    Docs: https://docs.mage.ai/guides/transformer-blocks#filter
    """

    # select wanted columns only
    df = df[['id', 'name', 'summary', 'longitude', 'latitude', 'space', 'description', 'instant_bookable', 'neighborhood_overview', 'neighbourhood_cleansed', 'host_id', 'host_name', 'host_since',
             'host_response_time', 'street', 'zipcode', 'review_scores_rating', 'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'reviews_per_month', 'amenities', 'cancellation_policy', 'number_of_reviews', 'price']]

    # remove $ sign from price column
    df['price'] = df['price'].str.replace(
        ',', '').str.replace('$', '').astype(float)


# # Identify string columns (object dtype) and fill them with 'N/A'
#     string_columns = df.select_dtypes(include=['object']).columns
#     df[string_columns] = df[string_columns].fillna('N/A')

    # Fill missing values with appropriate defaults
    df.fillna({'beds': 0, 'bedrooms': 0, 'bathrooms': 0, 'accommodates': 0,
               'reviews_per_month': 0, 'review_scores_rating': 0, 'price': 0, 'zipcode': 0}, inplace=True)

    df['host_since'] = df['host_since'].astype('datetime64')
    df['host_since'] = pd.to_datetime(df['host_since'], format='%Y-%m-%d')
    df['zipcode'] = pd.to_numeric(
        df['zipcode'], errors='coerce').astype('Int64')

    # remove rows with 0 beds , 0 bedrooms , 0 bathrooms , 0 accommodates , 0 reviews_per_month , 0 review_scores_rating
    df = df[(df['beds'] > 0) & (df['bedrooms'] > 0) & (df['bathrooms'] > 0) &
            (df['accommodates'] > 0) & (df['reviews_per_month'] > 0) &
            (df['review_scores_rating'] > 0) & (df['price'] > 0)]

    print(df.shape)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """

    assert output['beds'].isin([0]).sum() == 0, 'The output is undefined'

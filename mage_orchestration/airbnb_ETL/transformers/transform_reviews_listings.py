from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df: DataFrame, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    def detect_language(text):
        try:
            return detect(str(text))
        except:
            return None

    # apply to comment column
    df['language'] = df['comments'].apply(detect_language)
    # filter only english comments
    df = df[df['language'] == 'en']
    # sentiment analysis
    sentiment_analysis = SentimentIntensityAnalyzer()
    # apply to comment column to get sentiment scores
    df['sentiment_scores'] = df['comments'].apply(
        lambda x: sentiment_analysis.polarity_scores(x))
    df['pos'] = df['sentiment_scores'].apply(lambda x: x['pos'])
    df['neg'] = df['sentiment_scores'].apply(lambda x: x['neg'])
    df['neu'] = df['sentiment_scores'].apply(lambda x: x['neu'])
    df['compound'] = df['sentiment_scores'].apply(lambda x: x['compound'])
    # remove columns
    df.drop(columns=['sentiment_scores', 'language'], inplace=True)

    print(df.info())
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

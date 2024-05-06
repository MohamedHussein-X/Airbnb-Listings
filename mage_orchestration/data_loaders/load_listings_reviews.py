import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # import pandas as pd

    # URL of the CSV file on Google Drive (replace with your actual file URL)
    google_drive_csv_url = "https://drive.google.com/uc?id=1UtPJmGT58JYhrklf6MJB0ztAltb_iTEM"

    # parse_dates = 'host_since'
    # Read the CSV file directly from the URL using pandas
    reviews_df = pd.read_csv(google_drive_csv_url)

    # Now df contains the data from the CSV file
    print(reviews_df.head())  # Print the first few rows of the DataFrame

    return reviews_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

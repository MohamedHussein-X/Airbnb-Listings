from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import pandas as pd
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    # print files names of cuurent directory to check if the file is there
        # URL of the CSV file on Google Drive (replace with your actual file URL)
    google_drive_csv_url = "https://drive.google.com/uc?id=14YU77EpUtb1WsHfq6lz697JddbUa-v8O"

    # parse_dates = 'host_since'
    # Read the CSV file directly from the URL using pandas
    df = pd.read_parquet(google_drive_csv_url)
    print(df.info())
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'airbnb-listings-421017-bucket'
    object_key = 'reviews_polarized.parquet'

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
    )

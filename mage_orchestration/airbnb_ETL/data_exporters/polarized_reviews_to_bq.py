from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
import pandas as pd
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery

    """

    # print files names of cuurent directory to check if the file is there
    # URL of the CSV file on Google Drive (replace with your actual file URL)
    google_drive_csv_url = "https://drive.google.com/uc?id=14YU77EpUtb1WsHfq6lz697JddbUa-v8O"

    # parse_dates = 'host_since'
    # Read the CSV file directly from the URL using pandas
    df = pd.read_parquet(google_drive_csv_url)
    print(df['pos'].head(n=5))
    print(df.info())
    # cast DataFrame to BigQuery table
   # Cast DataFrame to BigQuery table
   # Ensure correct data types
   
    table_id = 'airbnb-listings-421017.Airbnb_dataset.reviews_polarized'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )

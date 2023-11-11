# Import required libraries/modules.
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

# Check if 'data_exporter' decorator is not already in the global namespace.
# Import 'data_exporter' decorator from 'mage_ai.data_preparation.decorators' if needed.
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# Define a data export function using the 'data_exporter' decorator.
@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """

    # Construct the path to the 'io_config.yaml' file and specify the configuration profile.
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Loop through the data items and export each DataFrame to BigQuery.
    for key, value in data.items():
        table_id = 'your_table_id.{}'.format(key)
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )

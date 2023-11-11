# Import required libraries/modules.
import io
import pandas as pd
import requests

# Check if 'data_loader' and 'test' decorators are not already in the global namespace.
# Import 'data_loader' and 'test' decorators from 'mage_ai.data_preparation.decorators' if needed.
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Define a data loading function using the 'data_loader' decorator.
@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API.
    """
    url = 'Your URL Data'
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')

# Define a testing function using the 'test' decorator.
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

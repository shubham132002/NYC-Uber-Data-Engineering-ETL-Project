# Import required libraries/modules.
import pandas as pd

# Check if 'transformer' and 'test' decorators are not already in the global namespace.
# Import 'transformer' and 'test' decorators from 'mage_ai.data_preparation.decorators' if needed.
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Define a transformer function using the 'transformer' decorator.
@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        df: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # Create datetime dimension
    datetime_dim = df[['tpep_pickup_datetime', 'tpep_dropoff_datetime']].drop_duplicates().reset_index(drop=True)
    datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
    # ... continue with other transformations ...

    # Create other dimensions (passenger_count_dim, trip_distance_dim, etc.)
    # ... continue with other transformations ...

    # Create fact table
    fact_table = df.merge(passenger_count_dim, on='passenger_count') \
             .merge(trip_distance_dim, on='trip_distance') \
             # ... continue with other merges ...

    # Return transformed data as a dictionary of dimension DataFrames and the fact table
    return {
        "datetime_dim": datetime_dim.to_dict(orient="dict"),
        "passenger_count_dim": passenger_count_dim.to_dict(orient="dict"),
        # ... include other dimensions ...
        "fact_table": fact_table.to_dict(orient="dict")
    }

# Define a testing function using the 'test' decorator.
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

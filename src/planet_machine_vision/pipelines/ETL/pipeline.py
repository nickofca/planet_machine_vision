"""
This is a boilerplate pipeline 'ETL'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import test_astroquery

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(test_astroquery,
             inputs="params:dummy_input",
             outputs=None)
    ])

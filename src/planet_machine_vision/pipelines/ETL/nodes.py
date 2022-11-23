"""
This is a boilerplate pipeline 'ETL'
generated using Kedro 0.18.3
"""
import astropy
from astroquery.simbad import Simbad



def test_astroquery(dummy_input):
    result_table = Simbad.query_object("M1")

    print(2)

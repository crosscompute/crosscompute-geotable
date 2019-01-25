import numpy as np
import pandas as pd
from crosscompute_geotable import routines


def test_get_display_bundle():
    t = pd.DataFrame([
        ('a', 0, 0),
        ('b', np.nan, np.nan),
    ], columns=['name', 'longitude', 'latitude'])
    packs, properties = routines.get_display_bundle(t)
    assert len(packs) == 1
    assert packs[0][0] == 1
    assert packs[0][1] == [0, 0]

    t = pd.DataFrame([
        ('a', 'POINT (0 0)'),
        ('b', 'POINT EMPTY'),
    ], columns=['name', 'wkt'])
    packs, properties = routines.get_display_bundle(t)
    assert len(packs) == 1
    assert packs[0][0] == 1
    assert packs[0][1] == [0, 0]

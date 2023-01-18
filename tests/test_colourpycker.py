from colourpycker.colourpycker import negative
import pandas as pd
import pytest

def test_negative():
    """Test that negative provides the right output."""
    expected = pd.DataFrame({
        'HEX' : ['#94604a', '#f6edf2', '#244176', '#c999d8', '#3eaadc'],
        'RGB' : [(148, 96, 74), (246, 237, 242), (36, 65, 118), (201, 153, 216), (62, 170, 220)]
    })

    actual = negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 5, 50)

    assert isinstance(actual, pd.DataFrame), \
        "Output is not a data frame."
    assert actual.columns[0] == expected.columns[0], \
        "Output data frame does not contain the column for HEX codes."
    assert len(actual.index) == 5, \
        "Output data frame does not contain the correct number of rows."
    assert expected['HEX'].iloc[0] == actual['HEX'].iloc[0], \
        "HEX code of most common colour is not correct."

    high_tol = negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 100, 100)
    
    assert len(high_tol.index) == 1, \
        "Setting tolerance to 100 should result in a maximum of 1 colour extracted."

    with pytest.raises(ValueError):
        negative("path/to/img.png", 4, 10)
        negative("https://upload.wikimedia.org/wikipedia/commons/8/89/HD_transparent_picture.png", 5, 100)
    
    with pytest.raises(TypeError):
        negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 4, 25.5)
        negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 4.8, 25)
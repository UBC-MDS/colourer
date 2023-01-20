import pandas as pd
from colourpycker.colourpycker import negative, get_color_palette
import pytest


def test_get_color_palette_valid_input():
    """Test for get_color_palette when input parameters are valid"""
    img_url = "https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg"
    tolerance = 20
    limit = 5
    result = get_color_palette(img_url, tolerance, limit)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 3)


def test_get_color_palette_not_a_url():
    """Test for get_color_palette when URL is a random string"""
    img_url = "soijfoidjfosdijfoisdj"
    tolerance = 20
    limit = 5
    result = get_color_palette(img_url, tolerance, limit)
    # Make sure no exception is raised and the function handles it
    assert result is None


def test_get_color_palette_url_but_not_image():
    """Test for get_color_palette when URL is valid but it is not pointing to an image"""
    img_url = "https://soijfoidjfosdijfoisdj.url"
    tolerance = 20
    limit = 5
    result = get_color_palette(img_url, tolerance, limit)
    # Make sure no exception is raised and the function handles it
    assert result is None


def test_get_color_palette_invalid_tolerance():
    """Test for get_color_palette when tolerance is invalid"""
    img_url = "https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg"
    tolerance = -20000
    limit = 5
    result = get_color_palette(img_url, tolerance, limit)
    # Make sure no exception is raised and the function handles it
    assert result is None

def test_negative():
    """Test that negative() generates the correct output and expects the right inputs."""
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
        "HEX code of the most common negative colour is not correct."
    assert expected['RGB'].iloc[0] == actual['RGB'].iloc[0], \
        "RGB code of the most common negative colour is not correct."
    
    # check inversion
    test_rgb = expected['RGB'].iloc[2]
    normal_rgb = (255 - int(test_rgb[0]), 255 - int(test_rgb[1]), 255 - int(test_rgb[2]))
    
    actual_rgb = actual['RGB'].iloc[2]
    actual_normal = (255 - int(actual_rgb[0]), 255 - int(actual_rgb[1]), 255 - int(actual_rgb[2]))

    assert actual_normal == normal_rgb, \
        "RGB code did not invert correctly."

    # maximum tolerance
    high_tol = negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 10, 100)
    # tolerance was set to a high value relative to the number of colours extracted
    moderate_tol = negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 20, 88)

    assert len(high_tol.index) == 1, \
        "Setting tolerance to 100 should result in a maximum of 1 colour extracted."
    assert len(moderate_tol.index) <= 20, \
        "Output data frame should have less than the specified number of colours."
   
    # partially transparent image
    partial = negative("https://i.stack.imgur.com/G4NCG.png", 20, 5)

    assert len(partial.index) == 1, \
        "Output data frame should contain one colour; partially transparent images should ignore transparent pixels."

    with pytest.raises(ValueError):
        # trying to read a path instead of a URL
        negative("path/to/img.png", 4, 10)
        # trying to extract colours from a transparent image
        negative("https://upload.wikimedia.org/wikipedia/commons/8/89/HD_transparent_picture.png", 5, 100)
    
    with pytest.raises(TypeError):
        # tolerance cannot be a float
        negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 4, 25.5)
        # number of colours cannot be a float
        negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 4.8, 25)
        # tolerance must be less than 100
        negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 5, 101)
        # tolerance cannot be 0
        negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 5, 0)
        # tolerance cannot be a negative integer
        negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 5, -10)

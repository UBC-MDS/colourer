from colourpycker import colourpycker
import pandas as pd


def test_get_color_palette_valid_input():
    """Test when input parameters are valid"""
    img_url = "https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg"
    tolerance = 20
    limit = 5
    result = colourpycker.get_color_palette(img_url, tolerance, limit)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (5, 3)


def test_get_color_palette_not_a_url():
    """Test when URL is a random string"""
    img_url = "soijfoidjfosdijfoisdj"
    tolerance = 20
    limit = 5
    result = colourpycker.get_color_palette(img_url, tolerance, limit)
    # Make sure no exception is raised and the function handles it
    assert result is None


def test_get_color_palette_url_but_not_image():
    """Test when URL is valid but it is not pointing to an image"""
    img_url = "https://soijfoidjfosdijfoisdj.url"
    tolerance = 20
    limit = 5
    result = colourpycker.get_color_palette(img_url, tolerance, limit)
    # Make sure no exception is raised and the function handles it
    assert result is None


def test_get_color_palette_invalid_tolerance():
    """Test when tolerance is invalid"""
    img_url = "https://soijfoidjfosdijfoisdj.url"
    tolerance = -20000
    limit = 5
    result = colourpycker.get_color_palette(img_url, tolerance, limit)
    # Make sure no exception is raised and the function handles it
    assert result is None

import numpy as np
import pandas as pd
from PIL import Image
from urllib.request import urlopen
import matplotlib.pyplot as plt
import extcolors


def get_color_palette(img_url, tolerance, limit):
    """
    Gets the color palette of an image

    Extracts the most common colors from an image
    and returns them as a dataframe of hex color codes and RGB values

    Parameters
    ----------
    img_url: str
        the url of the image from which the color palette is to be extracted
    tolerance: int
        a value between 0 and 100 representing the tolerance level for color matching
    limit: int
        the maximum number of colors to be returned in the palette

    Returns
    ----------
    dataframe
        a dataframe of hex color codes and RGB values corresponding to the most common colors in the image

    Examples
    --------
    get_color_palette('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', 20, 5)
    """


def donut(img_url, num_clrs, img_size):
    """Create a donut chart of the top n colors in the image (number of colors specified by the user)

    Creates a square donut chart using the n most common colors from the image

    Parameters
    ----------
    img_url: str
        the url of the image that the user is pulling the colors from
    num_clrs: int
        the number of colors the user wants to pull from the image
    img_size: int
        the pixel width and height of the resulting chart

    Returns
    ----------
    altair.vegalite.v4.api.Chart
        Donut chart of the colours

    Examples
    --------
    donut('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', 5, 400)
    """


def scatterplot(url, dataset, x, y, fill):
    """Create a two-dimensional scatterplot based on the colours of the image

    Creates a simple scatterplot using the colours selected from the image,
    plotting two features from a dataset of the users choosing.

    Parameters
    ----------
    url : str
        url of the image to extract colours
    dataset : pandas.DataFrame
        the dataset to plot (already imported)
    x: str
        the data to plot on the x-axis
    y: str
        the data to plot on the y-axis
    fill: str
        the data to use to fill in the points of the scatter plot

    Returns
    ----------
    altair.vegalite.v4.api.Chart
        Scatterplot using image colours

    Examples
    --------
    scatterplot('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', penguins, 'bill_length_mm', 'body_mass_g', 'species')
    """


def img_negative(input_img, num_colours=1, tolerance=10):
    """Invert top n colours in an image file.

    Colours are extracted from an image via URL

    Parameters
    ----------
    input_img : str
        URL of an image file.

    num_colours : int
        Number of colours to be extracted.

    tolerance : int
        Metric used to group colours together to give a better visual representation. Must be between 0 and 100.

    Returns
    -------
    pandas.DataFrame
        a table of the top n inverted colours in the image, including their HEX codes and occurrence (proportionate number of pixels)

    Examples
    --------
    >>> img_negative("https://t3.ftcdn.net/jpg/02/70/35/00/360_F_270350073_WO6yQAdptEnAhYKM5GuA9035wbRnVJSr.jpg", num_colours=3, tolerance=20)
    """

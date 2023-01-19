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


def donut(img_url, num_clrs, tolerance, img_size, plot_show=True):
    """Create a donut chart of the top n colors in the image (number of colors specified by the user)

    Creates a square donut chart using the n most common colors from the image

    Parameters
    ----------
    img_url: str
        the url of the image that the user is pulling the colors from
    num_clrs: int
        the number of colors the user wants to pull from the image
    tolerance: int
        a value between 0 and 100 representing the tolerance level for color matching
    img_size: int
        the pixel width and height of the resulting chart
    plot_show: bool
        set False to supress output of the chart

    Returns
    ----------
    matplotlib.figure.Figure
        Donut chart of the colours

    Examples
    --------
    donut('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', 5, 20, 400)
    """

    # get the top 100 colors and their proportion in the image
    df = get_color_palette(img_url, tolerance, limit=100)
    colors_prop = [round(x/sum(df['Color Count'].to_list()), 2) for x in df['Color Count'].to_list()]
    
    img_colors = df['HEX'].to_list()[0:num_clrs]
    img_colors.append("#a9a9a9")

    value = colors_prop[0:num_clrs]
    value.append(round(1-sum(value), 2))

    # need to do this to keep the donut hole in order
    factor = 0 # initialize the factor
    img_size = img_size/227 # macbook air resolution is 227 pixels/inch
    if img_size > 600/227:
        factor = 0.3
    elif img_size <= 200/227:
        factor = 0.7
    elif img_size <= 400/227:
        factor = 0.6
    elif img_size <=600/227:
        factor = 0.4

    category_value = []
    for i in range(len(img_colors)):
        category_value.append(img_colors[i] + ": "+ str(f'{value[i]*100:.0f}%'))
    
    # create the donut hole
    pie = plt.Circle( (0,0), radius=img_size*factor, color='white')

    # make labels
    labels = category_value[:-1]
    labels.append("Other colors: " + str(f'{value[-1]*100:.0f}%'))

    # label and color
    plt.pie(value, labels=labels, colors=img_colors, radius=img_size)
    p = plt.gcf()
    p.gca().add_artist(pie)

    if plot_show:
        plt.show()

    return p


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


def negative(img_url, num_colours=1, tolerance=100):
    """Invert top n colours in an image file.

    Colours are extracted from an image via URL and reversed,
    (e.g. red becomes cyan, green becomes magenta, yellow becomes blue)
    then stored in a table as HEX codes and RGB values.

    Parameters
    ----------
    img_url : str
        URL of an image file
    num_colours : int
        number of colours to be extracted
    tolerance : int
        number between 0 and 100 used to give better visual representation;
        0 will not group any similar colours together, 100 will group all colours into one

    Returns
    -------
    pandas.DataFrame
        a table of the top n inverted colours in the image, including their HEX codes and RGB values

    Examples
    --------
    >>> negative("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 3, 20)
    """

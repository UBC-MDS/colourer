import pandas as pd
from PIL import Image
import requests
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


def negative(img_url, num_colours=1, tolerance=0):
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
    if not img_url.startswith('https://'):
        raise ValueError("'img_url' must be a link (not a path).")

    if not [ext for ext in ['.png', '.jpg', '.jpeg'] if (ext in img_url)]:
        raise ValueError("'img_url' must be a direct link to an image file.")
    
    if not isinstance(num_colours, int):
        raise TypeError("'num_colours' must be an integer value.")

    if not isinstance(tolerance, int):
        raise TypeError("'tolerance' must be an integer value.")
    
    if not 0 <= tolerance <= 100:
        raise ValueError("'tolerance' must be between 0 and 100.")

    # Load image
    img = Image.open(requests.get(img_url, stream=True).raw)

    # Resize image for processing - 800 pixel maximum
    width = 800 / float(img.size[0])
    height = int((float(img.size[1]) * float(width)))
    img = img.resize((800, height), Image.LANCZOS)

    # Extract colours
    colours, pixel_count = extcolors.extract_from_image(img, tolerance=tolerance, limit=num_colours)
    
    # Check if there are any non-transparent pixels
    if not colours:
        raise ValueError("No coloured pixels detected in the image. It is likely transparent or something went wrong.")

    # Format RGB codes into list
    colour_list = str(colours).replace('[(', '').split(', (')
    rgb_list = [i.split('), ')[0] + ')' for i in colour_list]

    # Inverse RGB colour codes and extract HEX codes
    inversed_rgb = []
    hex = []
    for cols in rgb_list:
        rgb = cols.replace('(', '').replace(')', '').split(', ')
        inverse_code = (255 - int(rgb[0]), 255 - int(rgb[1]), 255 - int(rgb[2]))
        inversed_rgb.append(inverse_code)
        hex.append('#%02x%02x%02x' % inverse_code)

    # Format data frame
    df = pd.DataFrame({
        'HEX' : hex,
        'RGB' : inversed_rgb
    })
    print(hex)
    print(inversed_rgb)
    
    return df
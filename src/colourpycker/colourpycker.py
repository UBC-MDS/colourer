import numpy as np
import pandas as pd
from PIL import Image
from urllib.request import urlopen
import matplotlib.pyplot as plt
import extcolors


def img_negative(input_img, num_colours=1, tolerance=10):
    """Invert top n colours in an image file.

    Colours are extracted from an image via URL, where the maximum

    Parameters
    ----------
    input_img : str
        URL of an image file.

    num_colours : int
        Number of colours to be extracted.

    tolerance : int
        Metric to group colours to give a better visual representation. Must be between 0 and 100.

    Returns
    -------
    pandas.DataFrame
        a table of the top n colours including their HEX codes and occurrence in the photo (proportionate number of pixels)

    Examples
    --------
    >>> img_negative("https://t3.ftcdn.net/jpg/02/70/35/00/360_F_270350073_WO6yQAdptEnAhYKM5GuA9035wbRnVJSr.jpg", num_colours=3, tolerance=20)
    """
    # Load image
    img = Image.open(urlopen(input_img))
    colors, pixel_count = extcolors.extract_from_image(img)
    print(colors)
    print(pixel_count)
    # Resize image

    # plt.imshow(img)
    # plt.show()


# img_negative(
#     "https://t3.ftcdn.net/jpg/02/70/35/00/360_F_270350073_WO6yQAdptEnAhYKM5GuA9035wbRnVJSr.jpg",
#     num_colours=3,
#     tolerance=20,
# )

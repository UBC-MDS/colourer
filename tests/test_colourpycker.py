from colourpycker.colourpycker import donut
from colourpycker.colourpycker import get_color_palette
import numpy as np
import pandas as pd
import matplotlib.text as text

def test_donut():
    """Testing that donut() generates the correct output"""

    actual = len(donut("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 5, 30, 200, plot_show=False).findobj(text.Text))
    expect = 13
    assert actual == expect, "the function is not plotting the correct amount of colors"

    actual = str(type(donut("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 5, 30, 200, plot_show=False)))
    expect = "<class 'matplotlib.figure.Figure'>"
    assert actual == expect, "The function is not outputting a matplotlib figure"

    actual = str(donut("https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg", 5, 30, 200, plot_show=False).findobj(text.Text)[0:6][4])
    expect = "Text(0.9519963276938351, -0.18160370064393266, '#c9ba8f: 4%')"
    assert actual == expect, "the function is not returning the correct colors"
from colourpycker.colourpycker import scatterplot
import numpy as np
import pandas as pd
import altair as alt
import pytest

import pytest
def test_scatterplot():
    """Testing that the function scatterplot() generates the correct output and expects the right inputs.
    """
    #Creating a test dataframe
    test_df = pd.DataFrame({
        'x': np.array([1.1, 1.3, 2.4, 1.5, 1.9, 2.1, 2.1, 0.9, 3.1]),
        'y': np.array([6.8, 7.2, 9.4, 8.3, 5.4, 9.6, 2.9, 6.6, 4.3]),
        'fill': np.array(['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'])
    })
    
    #Creating a test plot
    test_scatter = scatterplot('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', test_df, 'x', 'y', 'fill', 50)
    
    # Tests
    assert test_scatter.mark == 'point', 'The mark should be a point'
    
    assert type(test_scatter)  == alt.vegalite.v4.api.Chart, "The return should be an altair Chart"
    
    assert test_scatter.encoding.fill.scale.range == ['#92b1b3', '#000800', '#ba754e'], "The fill of the points should be the colours from the image"
    
    assert test_scatter.encoding.x.field == 'x', "The x-axis of the points should be mapped to the x axis of the Chart"
    
    assert test_scatter.encoding.y.field == 'y', "The y-axis of the points should be mapped to the y axis of the Chart"
    
    with pytest.raises(TypeError):
        # x cannot be numeric
        scatterplot('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', test_df, 50, 'y', 'fill', 50)
        # y cannot be numeric
        scatterplot('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', test_df, "x", 50, 'fill', 50)
        # fill cannot be numeric
        scatterplot('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', test_df, "x", 'y', '50', 50)
        # tolerance cannot be cannot a float
        scatterplot('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', test_df, "x", 'y', '50', 50.75)
        
        

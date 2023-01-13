







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
        Scatterplot using image colours.
    
    Examples
    --------
    scatterplot('https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg', penguins, 'bill_length_mm', 'body_mass_g', 'species')
    """

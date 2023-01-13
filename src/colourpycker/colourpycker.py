







def scatterplot(url, x, y, fill, palatte):
    
    """Create a two-dimensional scatterplot based on the colours of the image
    
    Creates a simple scatterplot using the colours select 
    from the image based on a dataset of the users choosing.
    
    Parameters
    ----------
    url : str
        url to csv of data to plot
    x: str
        the data to plot on the x-axis
    y: str
        the data to plot on the y-axis
    fill: str
        the data to use to fill in the points of the scatter plot
    palatte: list
        the colour pallate obtained from from the image
    
    Returns
    ----------
    altair.vegalite.v4.api.Chart
        Scatterplot using image colours.
    
    Examples
    --------
    scatterplot(penguins, bill_length_mm, body_mass_g, species)
    """
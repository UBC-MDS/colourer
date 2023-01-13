




def donut(img_url, num_clrs, img_size):
    
    """Create a donut chart of the top n colors in the image (number of colors specified by the user)
    
    Creates a square donut chart using the n most common colors from the image 
    
    Parameters
    ----------
    img_url: str
        the url of the image that the user is pulling the colors from
    num_clrs: integer
        the number of colors the user wants to pull from the image
    img_size: integer
        the pixel width and height of the resulting chart
    
    Returns
    ----------
    colourpycker.donut
        Altair donut chart, specifically an altair.vegalite.v4.api.Chart
    
    Examples
    --------
    donut(https://visit.ubc.ca/wp-content/uploads/2019/04/plantrip_header-2800x1000_2x.jpg, 5, 400)
    """
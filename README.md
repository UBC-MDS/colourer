# colourpycker

A Python package that can be used to extract colours from images for use in data visualization projects.

## Overview

This package allows users to integrate unique colour palettes into their graphs for exploratory data analysis. The colours are retrieved from image data (via URL) and are selected based on their overall prominence in a picture. While there are existing tools that are used to process images and create figures independently, we aim to combine both of their functionalities to help programmers easily design effective and creative visualizations.

### Other similar Python libraries

There are packages in python that do similar functionality, as certain functions, but these packages require more than one package in order to do everything that we would like to do. 

For instance:

[Extcolors](https://pypi.org/project/extcolors/): This provides a color extraction into text along with the occurrence rate. However, with this package, we would need to use additional packages to create plots of common colours in the image. As well, this would not allow us to invert them, or create a palette.

[Color-extraction](https://pypi.org/project/color-extraction/): This provides the most similar color for the pixels of an image from a palette of predefined colors.

[Pylette](https://github.com/qTipTip/Pylette/): This extracts colours and creates colour palette based on an input image. This palette can be dumped in a a csv file. 

## Installation

```bash
$ pip install colourpycker
```

## Functions

`img_hex()`

`donut(img_url, num_clrs, img_size)`: This function creates a donut chart with information on the $n$ most common colors in the linked image. The user specifies the image, the number of colors, and specifies the size of the resulting chart.

`scatterplot(url, dataset, x, y, fill)`: Creates a simple scatterplot using the colours select from the image based on a dataset of the users choosing.
    

`img_negative(img_url, num_colours=1, tolerance=10)`: extracts the most common $n$ colours from an image (via URL) and inverts them to retrieve the negative version of a colour palette, returning the associated HEX codes and proportions in the image

## Usage

- TODO

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/colourpycker/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/colourpycker/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`colourpycker` was created by Shaun Hutchinson, Arjun Radhakrishnan, Alex Taciuk, and Lauren Zung. It is licensed under the terms of the MIT license.

## Credits

`colourpycker` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

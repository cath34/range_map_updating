# Range Map Updating

This repository contains the necessary code to reproduce the experiments for the range map updating project. To download the associated example dataset, please use the following [Google Drive link](https://drive.google.com/drive/folders/10eZc8-d6ECKrQEFdJjvUmVlHUKTuJYAB?usp=sharing). 

## License 

This repository is licensed under a
[MIT](https://opensource.org/license/mit). Please refer to our `LICENSE` file for further details. 

## Installation

You can import this repository in the form of a standalone package through pip using the following command 

```
pip install git+https://github.com/cath34/range_map_updating.git
```

If you prefer to download the repository on your local machine in a standard directory and run experiments from there, you can install the required packages from pip using `requirements.txt`.   


## Code

The `range_map_updating` folder contains the Python files to reproduce the experiments. 
* `range_map_updating/baseline_merow.py` : Implements the approach described in [*Merow et al.*](https://onlinelibrary.wiley.com/doi/abs/10.1111/geb.12539) (2016). 
* `range_map_updating/filter_observations.py` : Contains code to apply the same filters used by eBird for their Status and Trends Data Products (see [documentation](https://science.ebird.org/en/status-and-trends/faq#general2)). 
* `range_map_updating/geo_stats.py` : Contains code to compute location-based statistics on the observations and the range maps
* `range_map_updating/raster_utils.py` : Contains code to rasterize data based on a given AOI and grid cell size

## Notebook 

The `notebook` folder contains some interactive examples to show how to use the code. 
* `notebook/Range_Map_Updating_GeoStats.ipynb` : Shows how to compute location-based statistics using the functions available from the `range_map_updating/geo_stats.py` file. This notebook can also be accessed through the following [Google Colab Link](https://colab.research.google.com/drive/1xcdMWpKWnxuLa6lddmHHXCgn86ZWyHq3?usp=sharing). 


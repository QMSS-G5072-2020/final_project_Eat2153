# geocenpy 

![](https://github.com/elliotttrio/geocenpy/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/elliotttrio/geocenpy/branch/main/graph/badge.svg)](https://codecov.io/gh/elliotttrio/geocenpy) ![Release](https://github.com/elliotttrio/geocenpy/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/geocenpy/badge/?version=latest)](https://geocenpy.readthedocs.io/en/latest/?badge=latest)

This package helps users more easily visualize maps using Census Population Estimate API and the Census Cartographic GeoJSON boundary files. It transforms GeoJSON files into easy to work with GeoPandas.GeoDataFrame and plot choropleth maps. 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ geocenpy
```

## Dependencies

- pandas = "^1.1.5"
- pyproj = "^3.0.0"
- requests = "^2.25.1"
- numpy = "^1.19.4"
- shapely = "^1.7.1"
- gdal = [Wheels for Windows User](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal)
- fiona = [Wheels for Windows User](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona)
- geopandas = "^0.8.1"
- matplotlib = "^3.3.3"
- descartes = "^1.1.0"
- lxml = "^4.6.2"


## Usage

- For a complete guide and example usages, please go to `./GeoCenPyWriteUp.ipynb`.

## Documentation

The official documentation is hosted on Read the Docs: https://geocenpy.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/elliotttrio/geocenpy/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

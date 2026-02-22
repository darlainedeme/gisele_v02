# Gisele - Geospatial-based tool for electrification planning

## Introduction
Gisele is a powerful open-source tool for performing geospatial-based electrification planning. It is designed to assist in the decision-making process for extending and reinforcing electricity grids, with a focus on optimizing the grid layout and minimizing costs. Gisele uses a combination of geospatial data processing, clustering algorithms, and optimization techniques to identify the most effective electrification strategies.

## Features
- **Geospatial Data Processing:** Gisele can process a variety of geospatial data formats, including shapefiles, geojson, and raster data, to create a detailed representation of the study area.
- **Clustering:** The tool uses clustering algorithms to group together populated areas and identify potential locations for secondary substations.
- **Grid Routing:** Gisele can automatically route both medium-voltage (MV) and low-voltage (LV) grids, taking into account factors such as terrain, existing infrastructure, and load distribution.
- **Optimization:** The tool uses a Mixed-Integer Linear Programming (MILP) model to optimize the grid layout, considering factors such as cable costs, substation costs, and power losses.
- **Microgrid Analysis:** Gisele can also be used to evaluate the feasibility of microgrids as an alternative to grid extension, considering factors such as reliability and cost.
- **Customization:** The tool is highly customizable, allowing users to define their own electrical parameters, cost data, and optimization settings.

## Project Structure

The project is structured as a standard Python package:

```
├── gisele/                # Main Python package
├── scripts/               # Executable scripts
│   └── run_gisele.py      # Main script to run the tool
├── data/                  # Input data
├── docs/                  # Project documentation
│   └── ARCHITECTURE.md    # Documentation of the project architecture
├── tests/                 # Tests for the gisele package
├── setup.py               # Setup script for the gisele package
├── requirements.txt       # Python dependencies
├── environment.yml        # Conda environment file
├── README.md              # This file
└── ...
```

## Installation

To use Gisele, you will need to have a working Python environment. We recommend using a virtual environment to manage the project's dependencies.

**1. Clone the repository:**

```bash
git clone <repository-url>
cd gisele
```

**2. Create and activate a virtual environment:**

*Using `venv` (recommended for Python 3):*

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

*Using `conda`*

```bash
conda env create -f environment.yml
conda activate gisele
```

**3. Install the required dependencies:**

```bash
pip install -r requirements.txt
```

**4. Install the `gisele` package:**

To make the `gisele` package available for import, install it in editable mode:

```bash
pip install -e .
```

This will allow you to make changes to the source code and have them reflected immediately without reinstalling the package.

## Usage

The main entry point for running the Gisele tool is the `scripts/run_gisele.py` script. This script will guide you through the process of providing the necessary input data and configuring the tool's settings.

To run the tool, simply execute the following command:

```bash
python scripts/run_gisele.py
```

The script will then perform the electrification planning analysis based on the configuration and input data provided.

## Input Data

Gisele requires the following input data, which should be placed in the `data/` directory:

- **Electrical Parameters:** This includes the resistance, reactance, and maximum power of the cables that will be used, as well as the voltage of the grid. These parameters are defined in the `run_gisele.py` script.
- **Geospatial Data:** This includes the boundaries of the study area, the locations of existing substations, and the locations of populated areas. This data should be in a standard geospatial format, such as Shapefile or GeoJSON.
- **Configuration File:** The `data/Configuration.csv` file contains a variety of settings that control the behavior of the tool, such as the cost of electricity, the lifetime of the grid, and the desired level of reliability.

## Output Data

Gisele generates a variety of output files, which are saved in the `Case studies/<case_study_name>/Output/` directory. These include:

- **Shapefiles:** These files contain the optimized layout of the LV and MV grids, as well as the locations of the secondary substations.
- **Reports:** These files provide detailed information on the costs and performance of the grid, including the total cost of the grid, the cost per connection, and the expected power losses.
- **Visualizations:** These files provide a visual representation of the results, including maps of the optimized grid and charts showing the breakdown of costs.

## How it Works

The electrification planning process with Gisele can be broken down into the following steps:

1.  **Data Input:** The first step is to provide the tool with the necessary input data, including electrical parameters, geospatial data (e.g., cluster boundaries, substations, study area), and configuration files.
2.  **Geospatial Data Processing:** Gisele processes the input geospatial data to create a weighted grid of points that represents the study area. This grid is used to identify potential routes for the electricity grid.
3.  **Clustering:** The tool then uses a clustering algorithm to group together populated areas and identify potential locations for secondary substations.
4.  **LV and MV Grid Routing:** Once the substation locations have been identified, Gisele routes the LV and MV grids to connect the substations to the populated areas and to the main grid.
5.  **Optimization:** The next step is to optimize the grid layout using a Mixed-Integer Linear Programming (MILP) model. This model considers a variety of factors, such as cable costs, substation costs, and power losses, to identify the most cost-effective grid design.
6.  **Results Visualization:** Finally, the tool generates a variety of output files, including shapefiles of the optimized grid, reports on the costs and performance of the grid, and visualizations of the results.

## Contributing

We welcome contributions to the Gisele project. If you would like to contribute, please fork the repository and submit a pull request.

## License

Gisele is licensed under the MIT License. See the `LICENSE` file for more details.

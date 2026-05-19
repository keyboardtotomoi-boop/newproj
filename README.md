# Astronomical Data Scraper & Visualizer

Python programs for scraping astronomical observation data and creating visualizations on a Chromebook with Debian Linux.

## Features

- **Data Scraping**: Fetch astronomical data from public sources
- **Visualization**: Create sky maps, light curves, and distance plots
- **Data Storage**: Save observations to CSV files
- **Easy Setup**: Simple dependency management

## Prerequisites

- Debian Linux enabled on Chromebook
- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Open Terminal** on your Chromebook (in the Linux app)

2. **Clone or download this repository**:
   ```bash
   cd /home/user
   git clone https://github.com/keyboardtotomoi-boop/newproj.git
   cd newproj
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Scrape Astronomical Data

```bash
python3 scrape_astronomy.py
```

This will:
- Fetch space weather data
- Retrieve near-Earth asteroid information
- Save data to `asteroids_observations.csv`

### 2. Create Visualizations

```bash
python3 visualize_astronomy.py
```

This will generate example plots:
- `sky_map.png` - Star positions in the sky
- `asteroids.png` - Asteroid distances and velocities
- `light_curve.png` - Brightness changes over time

## Scripts

### `scrape_astronomy.py`
Scrapes astronomical data from public sources. Functions:
- `scrape_space_weather()` - Get solar activity data
- `scrape_asteroid_data()` - Get near-Earth asteroid info
- `save_observations_to_csv()` - Export data

### `visualize_astronomy.py`
Creates various astronomical visualizations. Functions:
- `plot_sky_coordinates()` - Plot stars on a sky map
- `plot_asteroid_distances()` - Compare asteroid distances/velocities
- `plot_light_curve()` - Show brightness changes
- `plot_constellation()` - Draw constellation patterns

## Next Steps

Some ideas to extend this:

- **Use NASA API**: Sign up for a free API key at https://api.nasa.gov/ for more data
- **Real-time tracking**: Add code to track ISS position
- **Spectral analysis**: Analyze starlight spectra
- **Observatory data**: Integrate with local observatory feeds
- **Web interface**: Create a simple Flask app to display results

## Troubleshooting

### ImportError when running scripts
Make sure you've activated the virtual environment:
```bash
source venv/bin/activate
```

### matplotlib display issues
On headless systems, matplotlib might fail. The scripts save to PNG files which work fine in any environment.

### Network errors
Some data sources require internet. Check your Chromebook's connection.

## Resources

- **Astropy Documentation**: https://docs.astropy.org/
- **NASA APIs**: https://api.nasa.gov/
- **NOAA Space Weather**: https://www.swpc.noaa.gov/
- **Minor Planet Center**: https://www.minorplanetcenter.net/

## License

Use freely for personal and educational purposes.

---

Happy stargazing! 🌟

"""
Astronomical Data Visualizer
Creates visualizations of astronomical observations
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from datetime import datetime
import csv

# Create output directory
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def plot_sky_coordinates():
    """Plot stars on a sky map (RA/Dec coordinates)"""
    print("Creating sky map visualization...")
    
    # Generate sample star data
    np.random.seed(42)
    n_stars = 100
    ra = np.random.uniform(0, 360, n_stars)  # Right Ascension (0-360°)
    dec = np.random.uniform(-90, 90, n_stars)  # Declination (-90 to 90°)
    magnitude = np.random.uniform(1, 6, n_stars)  # Brightness (lower = brighter)
    
    fig, ax = plt.subplots(figsize=(12, 8), projection='rectilinear')
    
    # Plot stars with brightness inversely proportional to magnitude
    sizes = (7 - magnitude) * 15  # Brighter stars = larger dots
    colors = plt.cm.YlOrRd(magnitude / 6)
    
    scatter = ax.scatter(ra, dec, s=sizes, c=magnitude, cmap='YlOrRd', 
                        alpha=0.6, edgecolors='white', linewidth=0.5)
    
    ax.set_xlabel('Right Ascension (degrees)', fontsize=12)
    ax.set_ylabel('Declination (degrees)', fontsize=12)
    ax.set_title('Sky Map - Star Positions', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 360)
    ax.set_ylim(-90, 90)
    ax.grid(True, alpha=0.3)
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Apparent Magnitude', fontsize=11)
    
    # Save figure
    output_path = OUTPUT_DIR / "sky_map.png"
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    print(f"✓ Saved sky map to {output_path}")
    plt.close()

def plot_asteroid_distances():
    """Plot asteroid distances and velocities"""
    print("Creating asteroid distance/velocity plot...")
    
    # Sample asteroid data
    asteroids = [
        {"name": "2024 AB1", "distance_km": 450000, "velocity_kms": 18.5},
        {"name": "2024 CD5", "distance_km": 1200000, "velocity_kms": 22.3},
        {"name": "2023 XY7", "distance_km": 800000, "velocity_kms": 19.8},
        {"name": "2023 AB3", "distance_km": 600000, "velocity_kms": 21.2},
        {"name": "2023 QW2", "distance_km": 950000, "velocity_kms": 20.5},
    ]
    
    names = [a["name"] for a in asteroids]
    distances = [a["distance_km"] / 1000 for a in asteroids]  # Convert to thousands of km
    velocities = [a["velocity_kms"] for a in asteroids]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Distance plot
    bars1 = ax1.bar(names, distances, color='steelblue', alpha=0.7, edgecolor='black')
    ax1.set_ylabel('Distance (1000 km)', fontsize=11)
    ax1.set_title('Near-Earth Asteroid Distances', fontsize=12, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.0f}', ha='center', va='bottom', fontsize=9)
    
    # Velocity plot
    bars2 = ax2.bar(names, velocities, color='coral', alpha=0.7, edgecolor='black')
    ax2.set_ylabel('Velocity (km/s)', fontsize=11)
    ax2.set_title('Near-Earth Asteroid Velocities', fontsize=12, fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    output_path = OUTPUT_DIR / "asteroids.png"
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    print(f"✓ Saved asteroid plot to {output_path}")
    plt.close()

def plot_light_curve():
    """Plot a sample light curve (brightness over time)"""
    print("Creating light curve visualization...")
    
    # Generate sample light curve data
    time_hours = np.linspace(0, 24, 100)
    # Simulate a variable star with sinusoidal brightness
    brightness = 10 + 2 * np.sin(time_hours / 4) + 0.5 * np.random.randn(100)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(time_hours, brightness, 'o-', color='darkblue', markersize=4, 
           linewidth=1.5, label='Observed Brightness')
    ax.fill_between(time_hours, brightness - 0.3, brightness + 0.3, 
                    alpha=0.2, color='blue', label='Uncertainty')
    
    ax.set_xlabel('Time (hours)', fontsize=12)
    ax.set_ylabel('Apparent Magnitude', fontsize=12)
    ax.set_title('Light Curve - Variable Star Brightness Over Time', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    ax.invert_yaxis()  # Invert because lower magnitude = brighter
    
    output_path = OUTPUT_DIR / "light_curve.png"
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    print(f"✓ Saved light curve to {output_path}")
    plt.close()

def plot_constellation():
    """Plot a sample constellation"""
    print("Creating constellation visualization...")
    
    # Orion constellation stars (sample RA/Dec)
    orion_stars = {
        "Betelgeuse": (88.8, 7.4, 0.4),
        "Rigel": (78.6, -8.2, 0.1),
        "Bellatrix": (81.3, 6.3, 1.6),
        "Alnitak": (85.3, -1.9, 1.9),
        "Alnilam": (86.0, -1.2, 1.7),
        "Mintaka": (83.0, -0.3, 2.2),
        "Saiph": (87.6, -9.7, 2.1),
    }
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Extract data
    names = list(orion_stars.keys())
    ra = [orion_stars[name][0] for name in names]
    dec = [orion_stars[name][1] for name in names]
    magnitude = [orion_stars[name][2] for name in names]
    
    # Plot stars
    sizes = (3 - np.array(magnitude)) * 100
    scatter = ax.scatter(ra, dec, s=sizes, c='yellow', alpha=0.8, 
                        edgecolors='white', linewidth=1.5)
    
    # Add star names
    for name, r, d in zip(names, ra, dec):
        ax.annotate(name, (r, d), xytext=(5, 5), textcoords='offset points',
                   fontsize=10, color='white', fontweight='bold')
    
    # Draw constellation lines (Orion's pattern)
    lines = [
        ("Betelgeuse", "Bellatrix"),
        ("Bellatrix", "Rigel"),
        ("Rigel", "Saiph"),
        ("Saiph", "Betelgeuse"),
        ("Alnitak", "Alnilam"),
        ("Alnilam", "Mintaka"),
    ]
    
    for star1, star2 in lines:
        r1, d1 = orion_stars[star1][0], orion_stars[star1][1]
        r2, d2 = orion_stars[star2][0], orion_stars[star2][1]
        ax.plot([r1, r2], [d1, d2], 'w--', alpha=0.5, linewidth=1)
    
    ax.set_xlabel('Right Ascension (degrees)', fontsize=12)
    ax.set_ylabel('Declination (degrees)', fontsize=12)
    ax.set_title('Orion Constellation', fontsize=14, fontweight='bold')
    ax.set_facecolor('navy')
    ax.grid(True, alpha=0.2, color='white')
    
    output_path = OUTPUT_DIR / "constellation.png"
    plt.savefig(output_path, dpi=100, bbox_inches='tight', facecolor='navy')
    print(f"✓ Saved constellation to {output_path}")
    plt.close()

def main():
    """Main visualization function"""
    print("=" * 50)
    print("Astronomical Data Visualizer")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    try:
        plot_sky_coordinates()
        plot_asteroid_distances()
        plot_light_curve()
        plot_constellation()
        
        print("=" * 50)
        print("Visualizations complete!")
        print(f"All files saved to: {OUTPUT_DIR.absolute()}")
        print("=" * 50)
    except Exception as e:
        print(f"✗ Error during visualization: {e}")

if __name__ == "__main__":
    main()

import os
os.environ['PROJ_LIB'] = "/Users/TONY/anaconda/share/proj/"
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd


# Extract the data we're interested in

# Price: the prices of home [# cites]
# latitude: [# cites]
# longitude: [# cities]
# center_lat, center_lon: [center of the map]
# area: the area of the circle
# take_log: take_log accross the prices
# Longitude requires a negative value!
def ViewInMap(price, lat, lon, center_lat, center_lon, area=None, take_log=True):
    # 1. Draw the map background
    if area is None:
        # If undefined area, use
        area = 20
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution='h',
                lat_0=center_lat, lon_0=center_lon,
                width=5E6, height=5.2E6)
    m.shadedrelief()
    m.drawcoastlines(color='gray')
    m.drawcountries(color='gray')
    m.drawstates(color='gray')

    # 2. scatter city data, with color reflecting prices
    # and size reflecting area
    if take_log:
        price = np.log10(price)
    m.scatter(lon, lat, latlon=True,
              c=price, s=area,
              cmap='Reds', alpha=0.5)
    # 3. create colorbar and legend
    plt.colorbar(label=r'$\log_{10}({\rm population})$')
    plt.clim(3, 7)
    # # make legend with dummy points
    # for a in [100, 300, 500]:
    #     plt.scatter([], [], c='k', alpha=0.5, s=a,
    #                 label=str(a) + ' km$^2$')
    # plt.legend(scatterpoints=1, frameon=False,
    #            labelspacing=1, loc='lower left');

if '__name__' == '__main__':
    cities = pd.read_csv('data/california_cities.csv')
    lat = cities['latd'].values
    lon = cities['longd'].values
    population = cities['population_total'].values
    area = cities['area_total_km2'].values
    USA_coordinates = [37.0902, -95.7129]
    ViewInMap(population, lat, lon, USA_coordinates[0], USA_coordinates[1], area=None)




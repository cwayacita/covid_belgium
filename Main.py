from matplotlib.figure import Figure

from AxesPlotter import AxesPlotter, PlotPattern
from DataAccessObject import DataAccessObject
from Enums import Country, PatientCase, PatientCategory
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dao = DataAccessObject(Country.belgium)

    # figure
    fig, ax = plt.subplots(figsize=(15, 10))

    # plotter
    ax_plotter = AxesPlotter(dao)

    # try to plot death
    ax_plotter.plot(ax, PlotPattern.death_country, cumsum=True, log=False)

    fig.autofmt_xdate()

    plt.show()
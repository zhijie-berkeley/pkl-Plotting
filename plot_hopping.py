# Python plot_hopping.py ../*.pkl
import functools
from pathlib import Path
from joblib import Memory
import matplotlib as mpl
from matplotlib import pyplot as plt
import mplcursors
from nucleosome_unzipping import __main__ as nu
import numpy as np
import mplcursors
from qtlib.types import OpenFilesType
from tweezers import api as tz, get_option

def main(filePath: Path, *,
         save: bool = False):
    print("reading...", filePath)
    name = str(filePath)[:-4]

    tr = tz.trace(filePath).get_downsampled_to(2500)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(tr.time, tr.dist, ".", color='red', alpha=.5, ms=2,
            lw=.5, label= name)
    ax2.plot(tr.time, tr.trap_sep*142, ".", color='blue',alpha=.5, ms=2,
    lw=.5, label= name)
    ax1.set(xlabel = "time (s)", ylabel = "bead distance (nm)", title = f"{name}.pkl")
    ax2.set(xlabel = "time (s)", ylabel = "trap_separation (nm)")

    mplcursors.cursor()
    if save:
        fig.savefig(f"{name}.png")
    else:
        plt.show()

if __name__ == "__main__":
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']
    # plt.rcParams["figure.figsize"] = (17.8/2.54, 8.7/2.54)
    plt.rcParams["font.size"] = 12

    import defopt
    defopt.run(main)
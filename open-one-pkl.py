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

# mem = Memory("/tmp/joblib")
# nu_main = mem.cache(nu.main)

def main(filePath: Path, *,
         save: bool = False):
    print("reading...", filePath)
    name = str(filePath)[:-4]

    tr = tz.trace(filePath)
    h = len(tr.dist) // 2
    nm_fwd = (tr.dist)[:h]
    nm_rvs = (tr.dist)[h:]
    f_fwd = (tr.force)[:h]
    f_rvs = (tr.force)[h:]
    fig, ax = plt.subplots()
    ax.plot(nm_fwd, f_fwd, ".", color='red', alpha=.5, ms=2,
            lw=.5, label= name, rasterized=True)
    ax.plot(nm_rvs, f_rvs, ".", color='blue',alpha=.5, ms=2,
    lw=.5, label= name, rasterized=True)
    ax.set(xlabel = "distance (nm)", ylabel = "force (pN)", title = f"{name}.pkl")

    mplcursors.cursor()

    if save:
        fig.savefig(f"{name}.png")

    else:
        plt.show()


if __name__ == "__main__":
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']
    plt.rcParams["figure.figsize"] = (17.8/2.54, 8.7/2.54)
    plt.rcParams["font.size"] = 10

    import defopt
    defopt.run(main)
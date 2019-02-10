import glob
import json

from matplotlib import pyplot as plt, transforms, pyplot
from matplotlib.colors import LogNorm


def plot_json(input_file, output_name, show=False):
    with open(input_file, ) as f:
        result_json = f.read()
    result = json.loads(result_json)
    x = []
    y = []
    for point in result['movements']:
        x.append(point[0])
        y.append(point[1])

    axes = plt.gca()
    axes.set_xlim([250, 1400])
    axes.set_ylim([0, 1400])

    # opencv coordinate systems is turned by 180° degree
    # not working though? :(
    # base_transformation = pyplot.gca().transData
    # rotation = transforms.Affine2D().rotate_deg(180)
    # transformation = base_transformation + rotation

    plt.plot(x, y)
    plt.savefig(output_name + '.plot.png')
    plt.hist2d(x, y, 20, norm=LogNorm())
    plt.colorbar()
    plt.savefig(output_name + '.histo.png')

    if show:
        plt.show()
    else:
        plt.clf()


json_files = glob.glob("results/**/*.json", recursive=True)

for json_file in json_files:
    print("Plotting file " + json_file)
    plot_name = json_file.replace(".json", "")
    plot_json(json_file, json_file)


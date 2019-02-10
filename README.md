# pigeon-tracker
Use Python and OpenCV to track pigeons for automated analysis of animal behavior experiments.

This repository currently mainly consists of some basic code for exploring the OpenCV capabilities.

## Depdencies
~~Installing `opencv3` from `menpo` repository should be enough for the examples to work in a miniconda environment.~~

Because of Python foobar, it's necessary to install `pango` from `asmeurer` repo when running on Fedora.

For getting mp4 playback to work, I've setup the conda environment with
```
conda install -c loopbio -c conda-forge -c pkgw-forge ffmpeg gtk2 opencv
```
On *Windows* you can ommit the `gtk2` package when using [Anaconda 5.3 Windows Installer](https://www.anaconda.com/download/)

The hard part was getting a working opencv version that's compiled with gtk2 and ffmpeg support.

## Jupyter

There is a kind of working Jupyter example, run it like this:
```
jupyter notebook example_notebook.ipynb 
```

Rendering of the video is very slow though, so it's only recommended for demo purposes.

# pigeon-tracker [![Build Status](https://travis-ci.com/neslihanedes/pigeon-tracker.svg?branch=master)](https://travis-ci.com/neslihanedes/pigeon-tracker)
Use Python and OpenCV to track pigeons (and other moving objects) for automated analysis of animal behavior experiments.

## Docker

The easiest way to get started is by simpling using the provided docker-compose file, which will automatically
build the corresponding Docker image:
```
docker-compose up
```

Please note, that this will also mount the project directory into the container, which runs on UID 0. This
will result in the root user owning files created by the container on Linux.

If you want to use rendered GTK windows, use `docker_run.sh`. Note that this needs an active X11 session on the host 
(or multiple quirks on Wayland, like setting `xhost +local:root`).

## Depdencies
Try to import the conda environment:
```
conda create --name pigeon-tracker --file spec-file.txt
conda activate pigeon-tracker
```

Because of Python foobar, it's necessary to install `pango` from `asmeurer` repo when running on Fedora 28.

### Manual Conda Dependency installation
Not recommended, but might give a hint when debugging non working environemnts.

For getting mp4 playback to work, you can setup the conda environment with
```
conda install -c loopbio -c conda-forge -c pkgw-forge ffmpeg gtk2 opencv
```
On *Windows* you can ommit the `gtk2` package when using [Anaconda 5.3 Windows Installer](https://www.anaconda.com/download/)

The hard part was getting a working opencv version that's compiled with gtk2 and ffmpeg support, so results may vary.

## Example Videos
Example videos are managed by [git-lfs](https://git-lfs.github.com/). They can be found under `example-videos/` and can 
be retrieved using git-lfs as well (which should happen automatically if correctly installed on the machine).

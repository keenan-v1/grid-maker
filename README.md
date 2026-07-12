# Grid Maker

## Install

Grid Maker is installed with [uv](https://docs.astral.sh/uv/). uv manages its
own Python and prefers prebuilt wheels, so you don't need system Python dev
headers or a compiler (which is what caused the old `pip install` to fail).

### Quick install (script)

```sh
curl -LsSf https://raw.githubusercontent.com/keenan-v1/grid-maker/main/install.sh | sh
```

The script bootstraps `uv` if it isn't already installed, then installs the
`gridmaker` CLI as a uv tool. If you've cloned the repo, you can instead run:

```sh
./install.sh
```

### Manual install with uv

```sh
uv tool install git+https://github.com/keenan-v1/grid-maker
```

Then see the help: `gridmaker -h`

> [!NOTE]
> If `gridmaker` isn't found after installing, run `uv tool update-shell` and
> open a new terminal so uv's tool bin directory is on your `PATH`.

### Run without installing

```sh
uvx --from git+https://github.com/keenan-v1/grid-maker gridmaker -h
```

## Usage
```
usage: grid.py [-h] [--width WIDTH] [--height HEIGHT] [--pixelsPerSquare PIXELSPERSQUARE] [--backgroundColor BACKGROUNDCOLOR] [--gridColor GRIDCOLOR] [--gridlineWidth GRIDLINEWIDTH] [--outputFileName OUTPUTFILENAME] [--colorList]

Generate a grid image

options:
  -h, --help            show this help message and exit
  --width WIDTH, -W WIDTH
                        The width of the grid in squares
  --height HEIGHT, -H HEIGHT
                        The height of the grid in squares
  --pixelsPerSquare PIXELSPERSQUARE, -s PIXELSPERSQUARE
                        The number of pixels per square
  --backgroundColor BACKGROUNDCOLOR, -b BACKGROUNDCOLOR
                        The background color of the grid.
  --gridColor GRIDCOLOR, -g GRIDCOLOR
                        The color of the gridlines.
  --gridlineWidth GRIDLINEWIDTH, -l GRIDLINEWIDTH
                        The width of the gridlines
  --outputFileName OUTPUTFILENAME, -o OUTPUTFILENAME
                        The name of the output file
  --colorList, -c       Output a list of colors to colors.png
  ```

> [!IMPORTANT]
> Grid lines are rectangles drawn inside the square. This effecitvely reduces the inner dimension of the square. For example, if your pixels per square size is the default of 70, and you use the default gridline width of 1, then the inner dimensions of the square will be 68x68.

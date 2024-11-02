# Grid Maker
## How to use
1. Make sure you have Python 3 installed.
2. Create a virtual environment: `python3 -m venv .venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the script: `python3 grid.py` or `./grid.py` on Linux and Mac

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

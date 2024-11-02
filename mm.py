import argparse
from PIL import Image, ImageDraw, ImageColor


def drawGrid(
    dimensions: tuple[int, int],
    pixelsPerSquare: int,
    backgroundColor: str,
    gridColor: str,
    gridlineWidth: int,
    outputFileName: str,
) -> None:
    width = (dimensions[0] * pixelsPerSquare) + (gridlineWidth * dimensions[0]) + gridlineWidth
    height = (dimensions[1] * pixelsPerSquare) + (gridlineWidth * dimensions[1]) + gridlineWidth
    img = Image.new("RGBA", (width, height), color=backgroundColor)
    draw = ImageDraw.Draw(img)
    for x in range(0, width, pixelsPerSquare):
        draw.line((x, 0, x, height), fill=gridColor, width=gridlineWidth)
    for y in range(0, height, pixelsPerSquare):
        draw.line((0, y, width, y), fill=gridColor, width=gridlineWidth)
    img.save(outputFileName)


def drawColorList() -> None:
    colors = ImageColor.colormap
    cols = 4
    rows = ((len(colors) - 1) // cols) + 1
    cellHeight = 30
    cellWidth = 170
    imageHeight = rows * cellHeight
    imageWidth = cols * cellWidth
    
    img = Image.new("RGBA", (imageWidth, imageHeight), color=0x0)
    draw = ImageDraw.Draw(img)
    for i, color in enumerate(colors.items()):
        x = (i % cols) * cellWidth
        y = (i // cols) * cellHeight
        draw.rectangle(
            [x, y, x + cellWidth, y + cellHeight],
            fill=color[1],
            outline=0x0,
        )
        draw.text(
            (x + 5, y + 5),
            f"{color[0]}: {color[1]}",
            fill=0x0,
        )
    img.save("colors.png")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a grid image")
    parser.add_argument(
        "--width",
        "-W",
        type=int,
        default=10,
        help="The dimensions of the grid",
    )
    parser.add_argument(
        "--height",
        "-H",
        type=int,
        default=10,
        help="The dimensions of the grid",
    )    
    parser.add_argument(
        "--pixelsPerSquare",
        "-s",
        type=int,
        default=10,
        help="The number of pixels per square",
    )
    parser.add_argument(
        "--backgroundColor",
        "-b",
        type=str,
        default="#00000000",
        help="The background color of the grid in RGBA hex format",
    )
    parser.add_argument(
        "--gridColor",
        "-g",
        type=str,
        default="#000000FF",
        help="The color of the grid lines in RGBA hex format",
    )
    parser.add_argument(
        "--gridlineWidth",
        "-l",
        type=int,
        default=1,
        help="The width of the grid lines",
    )
    parser.add_argument(
        "--outputFileName",
        "-o",
        type=str,
        default="grid.png",
        help="The name of the output file",
    )
    parser.add_argument(
        "--colorList",
        "-c",
        action="store_true",
        default=False,
        help="Output a list of colors to colors.png",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.colorList:
        drawColorList()
    else:
        drawGrid(
            dimensions=(args.width, args.height),
            pixelsPerSquare=args.pixelsPerSquare,
            backgroundColor=args.backgroundColor,
            gridColor=args.gridColor,
            gridlineWidth=args.gridlineWidth,
            outputFileName=args.outputFileName,
        )


if __name__ == "__main__":
    main()

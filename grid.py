#!/usr/bin/env python3

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
    width = (dimensions[0] * pixelsPerSquare)
    height = (dimensions[1] * pixelsPerSquare)
    img = Image.new("RGBA", (width, height), color=backgroundColor)
    draw = ImageDraw.Draw(img)
    for x in range(0, width, pixelsPerSquare):
        for y in range(0, height, pixelsPerSquare):
            draw.rectangle(
                [x, y, x + pixelsPerSquare - 1, y + pixelsPerSquare - 1],
                outline=gridColor,
                width=gridlineWidth,
            )
    img.save(outputFileName)


def drawColorList(outputFileName: str) -> None:
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
    img.save(outputFileName)


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
        default=70,
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
        default="",
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


def getOutputFileName(args: argparse.Namespace) -> str:
    fileName = args.outputFileName
    if not fileName or not fileName.endswith(".png"):
        if args.colorList:
            fileName = f"{fileName}colors.png"
        else:
            fileName = f"{fileName}grid_{args.width}x{args.height}_s{args.pixelsPerSquare}_l{args.gridlineWidth}.png"
    return fileName


def main() -> None:
    args = parse_args()
    if args.colorList:
        drawColorList(getOutputFileName(args))
    else:
        drawGrid(
            dimensions=(args.width, args.height),
            pixelsPerSquare=args.pixelsPerSquare,
            backgroundColor=args.backgroundColor,
            gridColor=args.gridColor,
            gridlineWidth=args.gridlineWidth,
            outputFileName=getOutputFileName(args),
        )


if __name__ == "__main__":
    main()

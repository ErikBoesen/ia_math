from PIL import Image, ImageDraw
import argparse
import sys

# Image sizes
SCALE = 400
WIDTH = SCALE
HEIGHT = SCALE

# Window bounds
REAL_START = -2
REAL_END = 1
IMAG_START = -1.5
IMAG_END = 1.5

ITER_LIM = 100

def mandelbrot(c):
    """
    Count iterations to convergence.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < ITER_LIM:
        z = z*z + c
        n += 1
    return n

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', dest='path', default='output.png', help='path to which to output image')
    args = parser.parse_args()

    image = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    for x in range(0, WIDTH):
        sys.stdout.write('\033[K')
        print('x=%d/%d (%d%%)\r' % (x, WIDTH, 100*x/WIDTH), end='')
        sys.stdout.flush()
        for y in range(0, HEIGHT//2+1):
            # Get complex number from coordinate
            c = complex(REAL_START + (x / WIDTH) * (REAL_END - REAL_START),
                        IMAG_START + (y / HEIGHT) * (IMAG_END - IMAG_START))
            m = mandelbrot(c)
            hsv = (140,
                   255,
                   int(255 * m / ITER_LIM) if m < ITER_LIM else 0)
            draw.point([x, y], hsv)
            draw.point([x, HEIGHT - y], hsv)

    image.convert('RGB').save(args.path, 'PNG')
    print('Image successfully saved to %s.' % args.path)

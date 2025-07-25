"""
Image Colormap
==============

Example showing simple plot creation and subsequent cmap change with Standard image from imageio.
"""

# test_example = true
# sphinx_gallery_pygfx_docs = 'screenshot'

import fastplotlib as fpl
import imageio.v3 as iio

im = iio.imread("imageio:camera.png")

figure = fpl.Figure(size=(700, 560))

# plot the image data
image_graphic = figure[0, 0].add_image(data=im, name="random-image")

figure.show()

image_graphic.cmap = "viridis"

# NOTE: fpl.loop.run() should not be used for interactive sessions
# See the "JupyterLab and IPython" section in the user guide
if __name__ == "__main__":
    print(__doc__)
    fpl.loop.run()

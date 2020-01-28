# Image_Sequence_Generation
The goal of this project is to write a program that can generate images representing sequences of numbers, for data augmentation purposes.

These images would be used to train classifiers and generative deep learning models. A script that saves examples of generated images is helpful in inspecting the characteristics of the generated images and in inspecting the trained models behaviours.

As a starting point, you may use images representing each
digit from the [MNIST database](http://yann.lecun.com/exdb/mnist/), and be
processed from the files coming from this website, using your own code.

To generate an image of a sequence, the digits have to be stacked horizontally
and the spacing between them should follow a uniform distribution over a range
determined by two user specified numbers. The numerical values of the digits
themselves are provided by the user and each digit in the generated sequence is
then chosen randomly from one of its representations in the MNIST dataset.

The width of the output image in pixels is specified by the user, while the
height should be 28 pixels (i.e. identical to that of the MNIST digits).  The
code should contain both an API and a script.

The function should look as follows:

```python
# A single function defined as follows:
def generate_numbers_sequence(digits, spacing_range, image_width):
    """
    Generate an image that contains the sequence of given numbers, spaced
    randomly using an uniform distribution.

    Parameters
    ----------
    digits:
	A list-like containing the numerical values of the digits from which
        the sequence will be generated (for example [3, 5, 0]).
    spacing_range:
	a (minimum, maximum) pair (tuple), representing the min and max spacing
        between digits. Unit should be pixel.
    image_width:
        specifies the width of the image in pixels.

    Returns
    -------
    The image containing the sequence of numbers. Images should be represented
    as floating point 32bits numpy arrays with a scale ranging from 0 (black) to
    1 (white), the first dimension corresponding to the height and the second
    dimension to the width.
```

And a script, to act as a command line tool to the above API. The script is
expected to use the above API, and accept the following parameters:

* sequence: the sequence of digits to be generated
* min spacing: minimum spacing between consecutive digits
* max spacing: maximum spacing between consecutive digits
* image width: width of the generated image

The generated image is saved in the current directory as a .png.

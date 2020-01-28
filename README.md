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

## Solution

The solution can be described in the following steps:
1. Load the MNIST data from keras.datasets.mnist
2. Create a list containing MNIST digits corresponding to each of the ten unique labels
3. Based on user specified spacing range and total width, spacing mode is either random or uniform. Get the corresponding spacing mode and gaps.
4. For each digit in user specified digit sequence, randomly select one of the images in MNIST corresponding to that label.
5. Horizontally append digit image and spacing gap.
6. Repeat step 4 and 5 for each digit in sequence and horizontally stack them to generate the sequence image.

Four scripts are provided:

1. An API is provided in "Digit_sequence_API.py"
2. A CLI script is provided in "Digit_sequence_CLI.py". 
This script takes command line arguements, then generates and saves the sequence image as png format in the current directory.
3. A test script is provided in "tests.py"
4. A utility script is provided in "MNIST_Digit_sequence.py"
5. A script containing logger description is provided in "Digit_sequence_generator_Logging.py"


## API 
'''
from Digit_sequence_API import Digits_sequence_API
api=Digits_sequence_API()
api.generate_sequence(digit_sequence,spacing_range)
api.save_sequence_image()
'''

where "digit_sequence" is the string containing digit sequence 
"spacing_range" is a tuple containing integer values for min gap and max gap
"generate_sequence" function returns an image of height 28 and width depending on random gap with 0 representing black and 255 representing white pixels
"save_sequence_image" saves the generated sequence image in the current directory with name as <digit_sequence>.png

## CLI

This script takes 4 arguements which are to be specified mandatorily.
usage: 

python Digit_sequence_CLI.py --digit_sequence DIGIT_SEQUENCE --min_gap MIN_GAP --max_gap MAX_GAP --total_width

DIGIT_SEQUENCE a string containing digit sequence
MIN_GAP: integer that specifies minimun gap between digits 
MAX_GAP: integer that specifies maximum gap between digits
TOTAL_WIDTH: integer specifying width of output image
example:

python Digit_sequence_CLI.py --digit_sequence 0965 --min_gap 0 --max_gap 10 --total_width 160

Note: Negative integers for MIN_GAP and MAX_GAP are treated as invalid values.



## Test

Ten tests are present in the tests.py

1. Loading of MNIST images
	-Check images height, width and number of classes 

2. Sequence image generation
	-Check image height
	-Check image width (in specified range)
	-Check datatype of pixels
	-Check pixel max and min value

3. Single digit sequence test
	-Check height and width of image 
	-Check datatype, min and max value of pixel

4. Invalid sequence test
	-Check if invalid sequence input generates "None" as output

5. Invalid spacing range test
	-Check if invalid spacing range generates "None" as output

6. Empty sequence test
	-Check if empty sequence as input generates "None" as output

7. Saving the generated image
	-Check if image is saved properly 

8. Checking random spacing mode
	-Check if random spacing mode is selected appropriately
	-Check if generated image is of desired dimension 

9. Checking uniform spacing mode
	-Check if uniform spacing mode is selected appropriately
	-Check if generated image is of desired dimension 

10. Checking invalid spacing range and total width combination
	-Check if invalid spacing range and total width combination is appropriately handled


Usage: python tests.py



## Loging:

Exceptions and other events are logged in "MNIST_Digit_sequence.log"
Logging is commented out as the print statements are suficient to provide the info in this case.


NOTE:
1. MNIST images loaded from Keras have black background as opposed to MNIST images obtained from website(http://yann.lecun.com/exdb/mnist/)
Hence for appending gap pixels between the digit images, background is first obtained.
2. Image_width parameter is eliminated from scripts to avoid ambiguity
3. Gap between the digits is random as specified.
4. The pixel values are between 0(black) and 255(white) and of datattype float32

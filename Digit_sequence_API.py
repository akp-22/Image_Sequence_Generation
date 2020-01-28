import cv2
from MNIST_Digit_sequence.lib.MNIST_Digit_sequence import MNIST_Digits_Sequence
import numpy as np

# API 
class Digits_sequence_API(object):
    # Constructor initialises the model to MNIST_Digits_Sequence model. 
    def __init__(self):
        self.sequence_generator_model = MNIST_Digits_Sequence()
    
    # Function to generate the image of digit sequence
    def generate_sequence(self,digits,spacing_range,total_width):
        self.digits=digits
        self.spacing_range=spacing_range
        self.Seq_image=self.sequence_generator_model.generate(digits,spacing_range,total_width)
        return self.Seq_image
    
    # Function to save the generated sequence image
    def save_sequence_image(self):
        if(np.any(self.Seq_image==None)):
            print("Image not saved.")
        else:
            cv2.imwrite(self.digits+".png",self.Seq_image)
            print("Image saved as "+ self.digits+".png")

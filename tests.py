# Test script defines 10 tests 

import numpy as np
from Digit_sequence_API import Digits_sequence_API
import os

class tests(object):
    def __init__(self):
        self.api=Digits_sequence_API()



#Loading of MNIST images
        
    def images_loading_test(self):
        classes=np.shape(self.api.sequence_generator_model.images)[0]
        w,h=np.shape(self.api.sequence_generator_model.images[0])[1:]
        return classes==10 and w==28 and h==28


#Sequence image generation
        
    def sequence_image_test(self):
        s="986"
        r=(0,10)
        w=100
        sequence=self.api.generate_sequence(s,r,w)
        size=np.shape(sequence)
        return (size[0]==28 and size[1]==w and np.amax(sequence)==255 and np.amin(sequence)==0 and sequence.dtype=="float32")


#3. Single digit sequence test
      
    def single_digit_sequence_test(self):
        s="9"
        r=(0,10)
        w=40
        sequence=self.api.generate_sequence(s,r,w)
        size=np.shape(sequence)
        return (size[0]==28 and size[1]==w and np.amax(sequence)==255 and np.amin(sequence)==0)


#4. Invalid sequence test
         
    def invalid_sequence_test(self):
        s="98s6"
        r=(0,10)
        w=100
        sequence=self.api.generate_sequence(s,r,w)
        return sequence==None


#5. Invalid spacing range test
         
    def invalid_spacing_range_test(self):
        s="1234"
        r=(np.pi,-3)
        w=200
        sequence=self.api.generate_sequence(s,r,w)
        return sequence==None


#6. Empty sequence test
       
    def empty_sequence_test(self):
        s=""
        r=(0,10)
        w=30
        sequence=self.api.generate_sequence(s,r,w)
        return sequence==None


#7. Saving the generated image
        
    def save_image_test(self):
        s="1234"
        r=(0,10)
        w=150
        sequence=self.api.generate_sequence(s,r,w)
        self.api.save_sequence_image()
        return os.path.isfile(s+".png")

#8. Checking the spacing range
    def random_spacing_test(self):
        s="1234"
        r=(0,10)
        w=150
        sequence=self.api.generate_sequence(s,r,w)
        shape=np.shape(sequence)
        return shape[0]==28 and shape[1]==w and self.api.sequence_generator_model.space_mode==1


#9. Checking spacing range for uniform case
    def uniform_spacing_test(self):
        s="1234"
        r=(0,10)
        w=130
        sequence=self.api.generate_sequence(s,r,w)
        shape=np.shape(sequence)
        return shape[0]==28 and shape[1]==w and self.api.sequence_generator_model.space_mode==0

#10 Checking invalid total width
    def invalid_total_width(self):
        s="1234"
        r=(0,10)
        w=10
        sequence=self.api.generate_sequence(s,r,w)
        return sequence==None and self.api.sequence_generator_model.space_mode==None


new_test=tests()
total_tests=10
test_passed=0


if(new_test.images_loading_test()):
    #print("Images loaded successfully")
    test_passed=test_passed+1
else:
    print("Test failed: MNIST Images not loaded correctly")


if(new_test.sequence_image_test()):
    #print("Sequence image generated successfully")
    test_passed=test_passed+1
else:
    print("Test failed: Sequence image not generated correctly")


if(new_test.invalid_spacing_range_test()):
    #print("Invalid spacing range handled correctly")
    test_passed=test_passed+1
else:
    print("Test failed: Invalid spacing range not handled correctly")
    

if(new_test.single_digit_sequence_test()):
    #print("Single digit image generated successfully")
    test_passed=test_passed+1
else:
    print("Test failed: Single digit image not generated correctly")


if(new_test.invalid_sequence_test()):
    #print("Invalid sequence handled correctly")
    test_passed=test_passed+1
else:
    print("Test failed: Invalid sequence not handled correctly")


if(new_test.empty_sequence_test()):
    #print("Empty sequence handled correctly")
    test_passed=test_passed+1
else:
    print("Test failed: Empty sequence not handled correctly")


if(new_test.save_image_test()):
    #print("Sequence image saved successfully")
    test_passed=test_passed+1
else:
    print("Test failed: Sequence image not saved correctly")

print("Tests passed: "+str(test_passed) + " out of "+ str(total_tests))


if(new_test.random_spacing_test()):
    #print("Sequence image saved successfully")
    test_passed=test_passed+1
else:
    print("Test failed: Random spacing case not handled correctly")


if(new_test.uniform_spacing_test()):
    #print("Sequence image saved successfully")
    test_passed=test_passed+1
else:
    print("Test failed: Uniform spacing case not handled correctly")



if(new_test.invalid_total_width()):
    #print("Sequence image saved successfully")
    test_passed=test_passed+1
else:
    print("Test failed: Invalid total width not handled correctly")

print("Tests passed: "+str(test_passed) + " out of "+ str(total_tests))













import argparse
from Digit_sequence_API import Digits_sequence_API

# Digits_sequence_API is API used to generate image of sequence of digits 
# 4 required user inputs are taken as command line arguments using a python parser object

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Arguements for digit sequence generation')
    parser.add_argument('--digit_sequence', default='000', required=True, type=str, help='Digit sequence')
    parser.add_argument('--min_gap', default=0, required=True, type=int, help='Minimum spacing between digits')
    parser.add_argument('--max_gap', required=True, type=int, help='Maximum spacing between digits')
    parser.add_argument('--total_width', required=True, type=int, help='Total width of output image')
    args = parser.parse_args()
    
    # API instance
    gen=Digits_sequence_API()
    # Function call to generate the sequence image
    image=gen.generate_sequence(args.digit_sequence,(args.min_gap,args.max_gap),args.total_width)
    # FUnction call to save the sequence image
    gen.save_sequence_image()
from utils import *
message = input("Please type your message\n")
flipped_message = flip(message)
num_a = count_letters(message, "a")
encoded_message = flipped_message + str(num_a)
print(f"Your encoded message is:{encoded_message}")
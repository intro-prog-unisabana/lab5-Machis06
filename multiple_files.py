from utils import *
message = input("Please type your message\n")
flipped_message = flip(message)
num_a = count_letters(message, "a")
encoded_message = flipped_message + ("a" * num_a)
print("Your ecoded message is:", encoded_message)
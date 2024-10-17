# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:25:14 2024

@author: -----
"""

# Function for interactive chatbot mode, dialoging directly
def chatbot_interactive():
    # Prompt the user to enter their gender and converts input to lowercase
    gender = input("Hello, are you male or female? ").lower()
    
    # Respond based on the user's gender
    if gender == 'female':
        print("How excellent! Are you a CS major?")
    elif gender == 'male':
        print("Me too. Are you a CS major?")
    else:
        # If the input is neither 'female' nor 'male', handle response as an unexpected input
        print(f"{gender.capitalize()}? Interesting. Are you a CS major?")
    
    # Prompt the user to answer if they are a CS major and converts input to lowercase
    major = input().lower()
    
    # Respond based on the user's answer about their major
    if major == 'yes':
        print("Excellent, I am too. What's an animal you don’t like, and two you do?")
    elif major == 'no':
        print("Too bad. Anyway, what's an animal you like, and two you don't?")
    else:
        # If the input is neither 'yes' nor 'no', handle it as an unexpected input
        print(f"{major.capitalize()}? Awesome! Moving on, what's an animal you like, and two you don't?")
    
    # Get the user's list of animals, separated by commas
    animals = input()
    # Split the input string by commas, remove extra spaces and convert to lowercase 
    animal_list = [animal.strip().lower() for animal in animals.split(",")]
    
    # Check if the user provided exactly three animals
    if len(animal_list) == 3:
        # Respond with a compliment for the third animal and agreement on disliking the first
        print(f"{animal_list[2].capitalize()} are awesome. But I hate {animal_list[0]} too. Bye for now.")
    else:
        # Default response for unexpected input
        print("Hmm, I've never heard of those animals. Bye for now.")
        
# Function to run the chatbot in file mode, reading responses from a file
def chatbot_from_file(file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            # Read all lines from the file into list
            lines = file.readlines()
        
        # Process the first line as the gender input, stripped of whitespace and converted to lowercase
        gender = lines[0].strip().lower()
        # Respond based on the gender input
        if gender == 'female':
            print("How excellent! Are you a CS major?")
        elif gender == 'male':
            print("Me too. Are you a CS major?")
        else:
            # Handle unexpected gender input
            print(f"{gender.capitalize()}? Interesting. Are you a CS major?")
        
        # Process the second line as the major input, stripped and converted to lowercase
        major = lines[1].strip().lower()
        # Respond based on the major input
        if major == 'yes':
            print("Excellent, I am too. What's an animal you don’t like, and two you do?")
        elif major == 'no':
            print("Too bad. Anyway, what's an animal you like, and two you don't?")
        else:
            # Handle unexpected major input
            print(f"{major.capitalize()}? Awesome! Moving on, what's an animal you like, and two you don't?")

        # Process the third line as the list of animals, stripped of whitespace
        animals = lines[2].strip()
        # Split the string by commas, remove extra spaces and convert to lowercase
        animal_list = [animal.strip().lower() for animal in animals.split(",")]
        
        # Check if there are exactly three animals in the list
        if len(animal_list) == 3:
            # Respond with a compliment for the third animal and agreement on disliking the first
            print(f"{animal_list[2].capitalize()} are awesome. But I hate {animal_list[0]} too. Bye for now.")
        else:
            # Default response for unexpected input
            print("Hmm, I've never heard of those animals. Bye for now.")
    
    # Handle case where the specified file is not found
    except FileNotFoundError:
        print(f"File {file_name} not found. Please check the file path.")
    # Handle case where the file does not contain enough lines
    except IndexError:
        print("File does not contain enough lines. Please ensure it has three lines of input.")

# Main function to choose the mode and run the appropriate mode function
def main():
    # Prompt the user to choose the mode: 'interactive' or 'file'
    mode = input("Enter 'interactive' for dialogue or 'file' to read from a file: ")
    
    if mode == 'interactive':
        # Call interactive method and run the interactive mode if the user chose 'interactive'
        chatbot_interactive()
    elif mode == 'file':
        # Prompt the user to enter the file name to be used as parameters for from file method
        file_name = input("Enter the file name: ")
        chatbot_from_file(file_name)
    else:
        # Inform the user of invalid mode choice
        print("Invalid mode. Please restart the program.")

# The main function is called to start the program        
if __name__ == "__main__":
    main()
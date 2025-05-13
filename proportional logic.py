known_facts = {
    "The sun rises in the east": True,
    "There are 3 days in a week": False,
    "Water boils at 100°C": True,
    "The Earth is flat": False,
    "Humans need oxygen to survive": True,
    "Python is a type of snake": False,
    "The sky is blue": True,
    "The moon is made of cheese": False,
    "Mount Everest is the highest mountain": True,
    "Birds can fly": True,
    "Fish can breathe underwater": True,
    "There are 365 days in a year": True,
    "The Earth revolves around the sun": True,
    "The capital of France is Berlin": False,
    "There are 24 hours in a day": True,
    "The ocean is made of water": True,
    "The Great Wall of China is visible from space": False,
    "The human body has 206 bones": True,
    "The Eiffel Tower is in London": False,
    "The Sun is a planet": False,
    "Sharks are mammals": False,
    "The capital of Japan is Tokyo": True,
    "There are 100 states in the USA": False,
    "The Amazon is the largest rainforest": True,
    "Mercury is the closest planet to the Sun": True,
    "The Sahara is the world's largest desert": True,
    "The speed of light is faster than sound": True,
    "Gravity keeps us on Earth": True,
    "The Great Barrier Reef is in the Pacific Ocean": True
}

def evaluate_statements(statement1: str, statement2: str) -> bool:
    """
    This function takes two statements, checks if both are true or false
    in the known facts dataset, and returns True or False accordingly.
    """
    # Check if the statements exist in the known facts
    if statement1 not in known_facts or statement2 not in known_facts:
        print("One or both statements are not in the known facts database.")
        return False
    
    # Evaluate both statements
    result1 = known_facts[statement1]
    result2 = known_facts[statement2]
    
    # If both facts are true or both are false, return True
    if result1 == result2:
        return True
    else:
        return False

def main():
    # User input for two statements
    print("Enter two statements to check if they are both true or false.")
    
    statement1 = input("Enter the first statement: ").strip()
    statement2 = input("Enter the second statement: ").strip()
    
    # Evaluate the statements
    result = evaluate_statements(statement1, statement2)
    
    # Output the result
    if result:
        print("True")
    else:
        print("False")

# Run the program
if __name__ == "__main__":
    main()
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # For "yes" answers
        self.right = None  # For "no" answers

def play_guessing_game(node):
    while node:
        if node.left and node.right:
            print(node.data)
            user_input = input("Enter 'yes' or 'no': ").strip().lower()

            if user_input == 'yes':
                node = node.left
            elif user_input == 'no':
                node = node.right
        elif node.left:
            print(node.data)
            user_input = input("Enter 'yes' or 'no': ").strip().lower()
            if user_input == 'yes':
                node = node.left
            else:
                print("Great! I guessed it.")
                return node.data  # Return the correctly guessed result
        else:
            print(f"Great! I guessed it.")
            return node.data  # Return the correctly guessed result

# Create the hierarchical tree structure
root = TreeNode("Is it a living thing?")
root.left = TreeNode("Is it an animal?")
root.right = TreeNode("Is it a non-living thing?")

# Living Things
root.left.left = TreeNode("Is it a mammal?")
root.left.right = TreeNode("Is it a reptile?")
root.left.left.left = TreeNode("Is it a carnivore?")
root.left.left.right = TreeNode("Is it a herbivore?")
root.left.right.left = TreeNode("Is it a snake?")
root.left.right.right = TreeNode("Is it a bird?")
root.left.left.left.left = TreeNode("Lion")
root.left.left.left.right = TreeNode("Tiger")
root.left.left.right.left = TreeNode("Python")
root.left.left.right.right = TreeNode("Rattlesnake")
root.left.right.left.left = TreeNode("Crocodile")
root.left.right.left.right = TreeNode("Snake")
root.left.right.right.left = TreeNode("Eagle")
root.left.right.right.right = TreeNode("Owl")

# Non-Living Things
root.right.left = TreeNode("Is it man-made?")
root.right.right = TreeNode("Is it found in nature?")
root.right.left.left = TreeNode("Is it a vehicle?")
root.right.left.right = TreeNode("Is it an electronic device?")
root.right.left.left.left = TreeNode("Car")
root.right.left.left.right = TreeNode("Bicycle")
root.right.left.right.left = TreeNode("Smartphone")
root.right.left.right.right = TreeNode("Laptop")
root.right.right.left = TreeNode("Is it a mineral?")
root.right.right.right = TreeNode("Is it a rock?")
root.right.right.left.left = TreeNode("Gold")
root.right.right.left.right = TreeNode("Diamond")
root.right.right.right.left = TreeNode("Granite")
root.right.right.right.right = TreeNode("Marble")

# Abstract Concepts
root.right.right.right.right = TreeNode("Sun")
root.right.right.right.left = TreeNode("Moon")
root.right.right.right.left.left = TreeNode("Time")
root.right.right.right.left.right = TreeNode("Love")

# Start the game from the root node
correct_guess = play_guessing_game(root)
print(f"The correctly guessed result is: {correct_guess}")


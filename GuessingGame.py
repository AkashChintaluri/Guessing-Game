class Node:
    def __init__(self, data):
        self.data = data
        self.yes_link = None
        self.no_link = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, game_file):
        with open(game_file, 'r') as file:
            self.root = self._build_tree_recursive(file)

    def _build_tree_recursive(self, file):
        line = file.readline().strip()
        if not line:
            return None

        data = line.split()
        node = Node(data[1])

        if data[0].isdigit():
            node.yes_link = self._build_tree_recursive(file)
            node.no_link = self._build_tree_recursive(file)

        return node

    def display_tree(self, order):
        if order == '1':
            self._inorder(self.root)
        elif order == '2':
            self._preorder(self.root)
        elif order == '3':
            self._postorder(self.root)
        else:
            print("Invalid order choice")

    def _inorder(self, node):
        if node:
            self._inorder(node.yes_link)
            print(node.data)
            self._inorder(node.no_link)

    def _preorder(self, node):
        if node:
            print(node.data)
            self._preorder(node.yes_link)
            self._preorder(node.no_link)

    def _postorder(self, node):
        if node:
            self._postorder(node.yes_link)
            self._postorder(node.no_link)
            print(node.data)

    def play_game(self):
        current_node = self.root
        while True:
            print(current_node.data)
            if not current_node.yes_link and not current_node.no_link:
                break

            answer = input("Enter your answer (Y/N): ").strip().lower()
            while answer not in ['y', 'n', 'yes', 'no']:
                print("Invalid input. Please enter 'Y' or 'N'.")
                answer = input("Enter your answer (Y/N): ").strip().lower()

            if answer in ['y', 'yes']:
                current_node = current_node.yes_link
            else:
                current_node = current_node.no_link

if __name__ == "__main__":
    binary_tree = BinaryTree()

    # Load the default game file
    binary_tree.build_tree("game1.txt")

    while True:
        print("\nMovie Guessing Game")
        print("P Play the game")
        print("L Load another game file")
        print("D Display the binary tree")
        print("X Exit the program")
        choice = input("...your choice: ").strip().lower()

        if choice == "p":
            binary_tree.play_game()
        elif choice == "l":
            file_name = input("Enter the file name to load: ")
            binary_tree.build_tree(file_name)
        elif choice == "d":
            order = input("What order do you want to display?\n1. Inorder\n2. Preorder\n3. Postorder\n... your choice: ")
            binary_tree.display_tree(order)
        elif choice == "x":
            break
        else:
            print("Invalid option. Please choose a valid option.")


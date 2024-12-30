from collections import deque
from helpers.problems import get_company_graph
from helpers.graph_tools import Tree


def breadth_first_search(tree: Tree, initial_state: str, goal="Morgan") -> tuple:
    """
    Performs a breadth-first search in a tree to find a goal node.

    Args:
        tree (Tree): The tree object containing the structure.
        initial_state (str): The root node of the tree.
        goal (str): Node label for which to search.

    Returns:
        tuple: (found, node_list) where:
            - found (bool): True if the goal node was found, else False.
            - node_list (list): A list of visited nodes in the order they were visited.

    Example:
        >>> breadth_first_search(tree, "Company", "Morgan")
        (True, ["Company", "Department_A", "Morgan"])
    """
    # Initialize the queue with the starting node
    queue = deque([initial_state])
    # List to keep track of the order in which nodes are visited
    node_list = []

    while queue:
        current_node = queue.popleft()
        node_list.append(current_node)
        
        # If the current node is the goal, return True and the visited nodes list
        if current_node == goal:
            return True, node_list
        
        # Get children of the current node and add them to the queue
        children = tree.get_children(current_node)
        queue.extend(children)
    
    # If we exit the loop without finding the goal, return False and all visited nodes
    return False, node_list


def depth_first_search(tree: Tree, initial_state: str, goal="Morgan", visited=None) -> tuple:
    """
    Performs a depth-first search in a tree to find a goal node.

    Args:
        tree (Tree): The tree object containing the structure.
        initial_state (str): The root node of the tree.
        goal (str): Node label for which to search.
        visited (list): List of visited nodes, used for recursion. Defaults to None.

    Returns:
        tuple: (found, node_list) where:
            - found (bool): True if the goal node was found, else False.
            - node_list (list): A list of visited nodes in the order they were visited.

    Example:
        >>> depth_first_search(tree, "Company", "Morgan")
        (True, ["Company", "Department_A", "Morgan"])
    """
    if visited is None:
        visited = []
    
    visited.append(initial_state)
    
    # If the current node is the goal, return True and the visited nodes
    if initial_state == goal:
        return True, visited
    
    # Explore each child recursively
    for child in tree.get_children(initial_state):
        if child not in visited:  # Ensuring the nodes are not revisited
            found, path = depth_first_search(tree, child, goal, visited)
            if found:
                return True, path
    
    # If goal was not found, return False and the visited nodes
    return False, visited


def get_student_credentials() -> str:
    """Returns the student's name for identification."""
    student_name = "Sayeeda Begam Mohamed Ikbal"
    return student_name


def main():
    """
    Main function to test the BFS and DFS implementations.
    """
    if get_student_credentials() == "Your name":
        print("Please set your name in get_student_credentials()!")
        return

    graph = get_company_graph()

    # Test case 1: Search starting from company to find "Morgan" with BFS
    print("Starting BFS from 'Company'")
    result, node_list = breadth_first_search(graph, initial_state="Company")
    print(result, node_list) 

    # Test case 2: Search starting from company to find "Morgan" with DFS
    print("Starting DFS from 'Company'")
    result, node_list = depth_first_search(graph, initial_state="Company")
    print(result, node_list) 

    # Feel free to add more test cases here

    # Test case 3: Search starting from 'Company' to find "Department_C" with BFS
    print("Starting BFS from 'Company' to find 'Department_C'")
    result, node_list = breadth_first_search(graph, initial_state="Company", goal="Department_C")
    print(result, node_list)  

    # Test case 4: Search starting from 'Company' to find a non-existent node "XYZ" with BFS
    print("Starting BFS from 'Company' to find 'XYZ'")
    result, node_list = breadth_first_search(graph, initial_state="Company", goal="XYZ")
    print(result, node_list) 

    # Test case 5: Search starting from 'Company' to find "Department_C" with DFS
    print("Starting DFS from 'Company' to find 'Department_C'")
    result, node_list = depth_first_search(graph, initial_state="Company", goal="Department_C")
    print(result, node_list)  

    # Test case 6: Search starting from 'Company' to find a non-existent node "XYZ" with DFS
    print("Starting DFS from 'Company' to find 'XYZ'")
    result, node_list = depth_first_search(graph, initial_state="Company", goal="XYZ")
    print(result, node_list)  

    # Test case 7: Search with a different starting node with BFS
    print("Starting BFS from 'Department_A' to find 'Morgan'")
    result, node_list = breadth_first_search(graph, initial_state="Department_A", goal="Morgan")
    print(result, node_list)  

    # Test case 8: Search with a different goal in a smaller graph with DFS
    print("Starting DFS from 'Department_A' to find 'Jordan'")
    result, node_list = depth_first_search(graph, initial_state="Department_A", goal="Jordan")
    print(result, node_list) 

    # Test case 9: Search a goal that does not exist with DFS
    print("Starting DFS from 'Department_A' to find 'NonExistentNode'")
    result, node_list = depth_first_search(graph, initial_state="Department_A", goal="NonExistentNode")
    print(result, node_list)  

if __name__ == "__main__":
    main()

def make_message(result, node_list):
    """Create a message from the result and node list"""
    if result:
        message = "Found! Path: "
    else:
        message = "Not found! Path: "
    message += " -> ".join(node_list)
    return message
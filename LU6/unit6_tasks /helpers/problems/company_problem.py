from helpers.graph_tools import Tree


def get_company_graph():
    """
    Creates a graph, representing a company.

    Returns:
        company_graph: The graph object.
    """
    company_graph_template = {
        "Company": ["Department_A", "Department_B", "Department_C"],
        "Department_A": ["Alex", "Jordan"],
        "Department_B": ["Casey", "Morgan"],
        "Department_C": ["Avery", "Taylor"],
    }

    company_graph = Tree(company_graph_template)

    return company_graph

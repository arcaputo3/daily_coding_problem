"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values,
which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
should return ['CSC100', 'CSC200', 'CSCS300'].
"""


def find_schedule(graph):
    """ Obtains sorted ordering of courses
        such that we can finish all courses. """

    out = []
    rec_stack = {g: False for g in graph}
    visited = {g: False for g in graph}

    def dfs(node):
        """ Performs dfs at a node and returns a bool representing
            whether or not we can continue.
            False: Graph has a Cycle - impossible to take all classes"""
        # Checks broken case, i.e. prereq not offered
        if node not in graph:
            return False

        # We have visted and need to recurse on this node
        visited[node] = True
        rec_stack[node] = True

        # List of prerequisites for this node
        for neighbor in graph[node]:
            # Course not offered, can't continue
            if node not in graph:
                return False

            if not visited[neighbor]:
                if not dfs(neighbor):
                    return False

            # Neighbor can't be reached
            elif rec_stack[neighbor]:
                return False

        out.append(node)
        rec_stack[node] = False
        return True

    for node in graph:
        if not visited[node]:
            if not dfs(node):
                return
    return out


if __name__ == "__main__":
    graph = {
        'CSC400': ['CSC100'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100', 'CSC400'],
        'CSC100': []
    }
    print(find_schedule(graph))

def chase_test(relation, decompositions):
    def closure(attributes, fds):
        closed_set = set(attributes)
        changed = True

        while changed:
            changed = False
            for fd in fds:
                if set(fd[0]).issubset(closed_set) and not set(fd[1]).issubset(closed_set):
                    closed_set.update(fd[1])
                    changed = True

        return closed_set

    for decomposition in decompositions:
        # Initialize the chase set with the attributes of the current decomposition
        chase_set = set(decomposition)

        while True:
            new_chase_set = set(chase_set)

            for fd in relation['fds']:
                # Check if the left side of the FD is in the current chase set
                if set(fd[0]).issubset(chase_set):
                    # Add the right side of the FD to the chase set
                    new_chase_set.update(fd[1])

            # If the chase set doesn't change, the decomposition is lossless
            if new_chase_set == chase_set:
                print(f"Decomposition {decomposition} is lossless.")
                break

            chase_set = new_chase_set

            # If the chase set contains all attributes, the decomposition is lossless
            if chase_set == set(relation['attributes']):
                print(f"Decomposition {decomposition} is lossless.")
                break
        else:
            print(f"Decomposition {decomposition} is not lossless.")

# Example usage
relation = {
    'attributes': ['A', 'B', 'C', 'D'],
    'fds': [(['B'], ['AD'])]
}

decompositions = [['A', 'D'], ['B', 'C'], ['C', 'D']]

chase_test(relation, decompositions)
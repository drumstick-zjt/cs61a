def chain(t):
    """
    Returns whether there exists a path in t where all nodes
    share the same label.
    >>> all_fives = Tree(5, [Tree(5), Tree(5, [Tree(5)])])
    >>> chain(all_fives)
    True
    >>> t1 = Tree(1, [Tree(3, [Tree(4)]), Tree(1)])
    >>> chain(t1)
    True
    >>> t2 = Tree(1, [Tree(3, [Tree(4)]), Tree(5)])
    >>> chain(t2)
    False
    """
    def recursive_helper(t, label):
        if not t:
            return True
        if t.is_leaf():
            return t.label == label
        else:
            for t in t.branches:
                if recursive_helper(t, label):
                    return True
            return False
    
    if not t:
        return True
    else:
        return recursive_helper(t, t.label)


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

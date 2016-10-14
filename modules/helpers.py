# https://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression
def mergeDicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z
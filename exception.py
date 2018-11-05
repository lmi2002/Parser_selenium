class ElementNotFoundException(Exception):
    def __init__(self, item, cause=None):
        super(ElementNotFoundException, self).__init__()
        self.item = item
        self.cause = cause

    def __str__(self):
        return "The element with {0} '{1}' was not found".format(*self.item)
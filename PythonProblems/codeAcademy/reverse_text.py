# Without using the reverse keyword
def reverse(text):
    return "".join([string[-i] for i in xrange(1,len(text)+1)])
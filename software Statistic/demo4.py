import logging
logging.basicConfig(level = logging.INFO)

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    # assert n!=0,'n is zero'
    logging.info('n=%d' % n)
    return 10/n

foo(0)



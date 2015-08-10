# Useful utilities

import sys
import traceback

__author__ = 'rohe0002'


def exception_trace(tag, exc, log=None):
    message = traceback.format_exception(*sys.exc_info())
    if log:
        log.error("[%s] ExcList: %s" % (tag, "".join(message),))
        log.error("[%s] Exception: %s" % (tag, exc))
    else:
        print >> sys.stderr, "[%s] ExcList: %s" % (tag, "".join(message),)
        print >> sys.stderr, "[%s] Exception: %s" % (tag, exc)


def to_unicode(b):
    """
    Convert a byte string to an unicode string
    :param b: byte string
    :return: unicode string
    """
    try:
        b = b.decode()
    except AttributeError:
        pass
    return b

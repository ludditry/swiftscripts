#!/usr/bin/env python

# in the future, this will be pluggable and load a function from
# config, perhaps also passing kwargs through.  For example, I could
# have a function 'mail' that has some extra config (from, to, not
# sure how subject will work yet.)


levels=["info", "error", "debug", "warn", "critical"]

def info(s, **kwargs):
    kwargs['level'] = 'info'
    output(s, **kwargs)


def debug(s, **kwargs):
    kwargs['level'] = 'debug'
    output(s, **kwargs)


def error(s, **kwargs):
    kwargs['level'] = 'error'
    output(s, **kwargs)


def warn(s, **kwargs):
    kwargs['level'] = 'warn'
    output(s, **kwargs)


def critical(s, **kwargs):
    kwargs['level'] = 'critical'
    output(s, **kwargs)


def output(s, **kwargs):
    level = kwargs.get('level')
    if level:
        print "%s: %s" % (level.upper(), s)
    else:
        print s

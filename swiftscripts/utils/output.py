#!/usr/bin/env python

# in the future, this will be pluggable and load a function from
# config, perhaps also passing kwargs through.  For example, I could
# have a function 'mail' that has some extra config (from, to, not
# sure how subject will work yet.)


def output(s, **kwargs):
    print s

#!/usr/bin/python

from ConfigParser import ConfigParser


def get_conf(section=None):
    c = ConfigParser()
    try:
        # TODO: maybe add some cli parsing
        conf_path = sys.argv[1]
    except Exception:
        conf_path = "/etc/swift/swiftscripts.conf"
    if not c.read(conf_path):
        print "Unable to read config file %s" % conf_path
        sys.exit(1)
    if section is not None:
        conf = dict(c.items(section))
    else:
        conf = {}
        for section in conf.sections():
            conf[section] = dict(c.items(section))
    return conf

#!/usr/bin/env python

from swift.common.utils import whataremyips
from swift.common.ring import Ring


def whataremyactivelabels(ring_files=None, swift_conf_dir="/etc/swift"):
    """Read ring_files and extract a set of paths that should be on the
host running this script.

    Keyword arguments:
    ring_files -- a list of filenames containing the rings to scan.
        (default:  ["/etc/swift/object.ring.gz,
                    "/etc/swift/account.ring.gz,
                    "/etc/swift/container.ring.gz"]
    swift_conf_dir -- the base path for swift config. (default: "/etc/swift")
    """
    # takes an optional list of filenames to use as the ring files
    # returns a list of paths that should be mounted under swift_path
    if ring_files is None:
        rings_files = ["/etc/swift/%s.ring.gz" % thing for thing in
                       ["object", "container", "account"]]
    my_ips = whataremyips()
    devices = set()
    for ring_file in rings_files:
        ring = Ring(ring_file)
        devices.update([entry['device'] for entry in ring.devs
                        if float(entry['weight']) > 0 and
                        entry['ip'] in my_ips])
    return devices

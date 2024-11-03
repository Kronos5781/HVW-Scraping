#! /usr/bin/env python3

from hch.apps.autoreporter import AutoReporter
from hch.conf import auto_reporter_conf


def main():

    auto_reporter_conf.USE_LOCAL_DATA_ONLY = True

    autoreporter = AutoReporter()
    autoreporter.run()


if __name__ == "__main__":
    main()

#coding:utf_8

"""
missing module docstring
"""

import argparse

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description='Safe Tls client and server')
    PARSER.add_argument('-H', '--host', help='hostname or IP address')
    PARSER.add_argument('-p', '--port', type=int, help='TCP port number')
    PARSER.add_argument('-a', metavar='cafile', default=None, help='authority')
    ARGS = PARSER.parse_args()
    print ARGS.host, ARGS.port, ARGS.a

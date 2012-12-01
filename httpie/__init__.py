"""
HTTPie - a CLI, cURL-like tool for humans.

"""
__author__ = 'Jakub Roztocil'
__version__ = '0.4.0-alpha'
__licence__ = 'BSD'


class exit:
    OK = 0
    ERROR = 1
    ERROR_TIMEOUT = 2

    # Used only when requested with --check-status:
    ERROR_HTTP_3XX = 3
    ERROR_HTTP_4XX = 4
    ERROR_HTTP_5XX = 5

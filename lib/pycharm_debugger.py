try:
    import pydevd_pycharm
    pydevd_pycharm.settrace('localhost', port=50059, stdoutToServer=True, stderrToServer=True)
except ImportError:
    pass

import sys
import signal

def signal_handler_exit(signal, frame):
    """
    Signal handler function to exit the program
    """
    sys.exit()

def signal_handler():
    """
    Set up signal handlers for Ctrl+C
    """
    signal.signal(signal.SIGINT, signal_handler_exit)
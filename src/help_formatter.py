import argparse

class HelpFormatter(argparse.HelpFormatter):
    def format_help(self):
        help_text = super().format_help()
        help_text = "Usage: mris [options] file\n\n"
        help_text = help_text + "Options:\n"
        help_text = help_text + "  -h, --help\t\tShow this help message and exit\n"
        help_text = help_text + "  -d, --debug\t\tEnable debug mode\n"
        help_text = help_text + "  -t, --test <file>\tProgram verification\n"
        return help_text
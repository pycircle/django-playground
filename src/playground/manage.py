import os
import sys


def main():
    #os.chdir(os.environ.get('PLAYGROUND_DIR'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playground.playground.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

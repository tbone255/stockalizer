#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#root_path = os.path.abspath(os.path.split(__file__)[0])
#print(root_path)
#sys.path.insert(0, os.path.join(root_path, 'stockalyzer'))
#sys.path.insert(0, root_path)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockalyzer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

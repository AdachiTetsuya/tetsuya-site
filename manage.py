#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

    load_dotenv(dotenv_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tetsuya_site.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

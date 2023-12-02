#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


try:
    import setuptools
except ImportError as error:
    print("ERROR: Can not execute `setup.py` since setuptools is not available in",
          "the build environment.",
          file=sys.stderr,
          )
    sys.exit(1)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Myproject.settings')
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


    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        print("ERROR: Django is not installed. Please install it using pip install django`.")
        sys.exit(1)

    execute_from_command_line(sys.argv)

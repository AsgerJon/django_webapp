#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen

import os
import sys


def main() -> None:
  """Run administrative tasks."""
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_webapp.settings')
  try:
    from django.core.management import execute_from_command_line
  except ImportError as exc:
    e = """Failed to import Django."""
    raise ImportError(e) from exc
  execute_from_command_line(sys.argv)


if __name__ == '__main__':
  main()

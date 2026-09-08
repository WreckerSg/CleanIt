#!/usr/bin/env python
"""Punto de entrada de Django desde la raíz del repositorio."""

import os
import sys
from pathlib import Path


if __name__ == "__main__":
    source_directory = Path(__file__).resolve().parent / "src"
    sys.path.insert(0, str(source_directory))
    os.chdir(source_directory)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

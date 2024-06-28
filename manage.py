#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

# BASE_DIR을 정의합니다
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# .env 파일 경로를 정의합니다
dotenv_path = os.path.join(BASE_DIR, '.env')

# .env 파일을 로드합니다
load_dotenv(dotenv_path)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snowlive.settings')
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

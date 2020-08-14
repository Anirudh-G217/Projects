#!/usr/bin/env python
'''
Automatically created for each Django project.
Sets the DJANGO_SETTINGS_MODULE environment variable so that it
points to your project’s settings.py file.

'''
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'database_chatbot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) 
    execute_from_command_line(sys.argv)

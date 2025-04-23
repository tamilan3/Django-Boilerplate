import os
from dotenv import load_dotenv

# Django project package initializer
# Load environment variables from a .env file
load_dotenv()

# Example: Set default settings based on environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Dynamically load URL based on environment
BASE_URL = os.getenv('BASE_URL', 'http://localhost:8000')
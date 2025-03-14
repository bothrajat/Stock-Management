#!/bin/sh

# Exit script on error
set -e

# Check if database initialization flag exists
if [ ! -f "/app/db_initialized" ]; then
    echo "Running initial setup..."
    python manage.py migrate
    python manage.py updatemodels
    touch /app/db_initialized
else
    echo "Running migrations..."
    python manage.py migrate
fi

# Start the Django server
exec "$@"

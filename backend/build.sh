#!/usr/bin/env bash
# Build script for Render.com deployment
# This runs during the build phase

set -o errexit  # Exit on error

echo "=== Installing Python dependencies ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Creating database tables ==="
python create_db.py

echo "=== Creating admin user ==="
python create_admin.py

echo "=== Build complete ==="

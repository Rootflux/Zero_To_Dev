#!/bin/bash
echo 'Installing requirements...'
pkg install -y python
pip install requests
echo 'Setup complete. Add your OPENWEATHER_API_KEY to environment variables.'

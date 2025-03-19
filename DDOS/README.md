# HTTP Request Simulator

A simple Python tool that simulates multiple users sending concurrent HTTP requests to a target server.

## Overview

This script creates multiple threads to send HTTP GET requests to a specified target URL. It's useful for basic load testing, website monitoring, or simulating multiple users accessing a web resource simultaneously.

## Features

- Multi-threaded request sending
- Continuous request loop until an error occurs
- Configurable number of concurrent threads
- Built-in logging of responses and errors

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Ensure Python 3.x is installed on your system
2. Install the required package:
   ```
   pip install requests
   ```

## Usage

1. Set the target URL in the `target` variable
2. Configure the number of threads using the `num_threads` variable
3. Run the script:
   ```
   python request_simulator.py
   ```

## Configuration Options

- `target`: The URL to send requests to (currently empty - must be specified)
- `num_threads`: Number of concurrent threads to create (default: 10)
- `logging.basicConfig`: Configure logging level and format

## How It Works

1. The script initializes logging to display information about requests
2. Each thread runs the `send_request()` function which:
   - Continuously sends GET requests to the target URL
   - Logs the HTTP status code of each response
   - Stops if an error occurs
3. The main thread waits for all worker threads to complete

## Warning

⚠️ This script will continuously send requests until an error occurs. Be cautious when using it against production servers, as it may:
- Create excessive load on the target server
- Trigger rate limiting or IP blocking
- Consume significant bandwidth

Always ensure you have permission to perform load testing on the target system.

## Customization

You can modify the script to:
- Add delays between requests
- Use different HTTP methods (POST, PUT, etc.)
- Send custom headers or payloads
- Implement more sophisticated error handling
# Redis Cache Module

## Overview

This module provides a `Cache` class for interacting with a Redis NoSQL database. It includes functionality to store and retrieve data, track method calls, and display call history.

## Features

- **`Cache` Class**: A class for storing and retrieving data from Redis.
- **Call Tracking**: Decorators to count method calls and track method call history.
- **Replay Function**: Displays the call history of methods in the `Cache` class.

## Installation

Make sure you have Redis installed and running. You can install the required Python packages using:

```bash
pip install redis

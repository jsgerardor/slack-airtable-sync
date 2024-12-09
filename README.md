# ioet-houses-bot

## Overview

The `ioet-houses-bot` is a Slack bot listener designed to integrate with Airtable for managing and tracking points within a Slack workspace. The bot listens to specific events in Slack and updates an Airtable table accordingly. This application is built using Python and leverages the Slack Bolt framework for handling Slack events and interactions.

## Features

- **Slack Integration**: Listens to events and messages in Slack channels.
- **Airtable Integration**: Updates and retrieves data from an Airtable base.
- **Karma Tracking**: Manages and tracks points for users based on Slack interactions.

## Requirements

- Python 3.10 or higher
- Slack API tokens
- Airtable API key

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:jsgerardor/slack-airtable-sync.git
    cd slack-airtable-sync
    ```

2. Create a virtual environment
    ```sh
    python3 -m venv .venv
    ```

3. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

4. Create a `.env` file with the necessary environment variables:
    ```env
    HOUSES_SLACK_BOT_TOKEN=your-slack-bot-token
    HOUSES_SLACK_APP_TOKEN=your-slack-app-token
    KARMA_CHANNEL_ID=your-karma-channel-id
    AIRTABLE_BASE_ID=your-airtable-base-id
    AIRTABLE_TABLE_NAME=your-airtable-table-name
    AIRTABLE_API_KEY=your-airtable-api-key
    LLM_API_KEY=your-llm-api-key
    ```

## Usage

Run the bot using Poetry:
```sh
python3 -m main
```

The bot will start listening to events in the specified Slack workspace and update the Airtable base accordingly.

## Docker

### Build and Run with Docker

1. Build the Docker image:
    ```sh
    make build
    ```

2. Run the Docker container:
    ```sh
    make run
    ```

3. Stop the Docker container:
    ```sh
    make stop
    ```

4. Remove the Docker container:
    ```sh
    make rm
    ```

5. Rebuild and run the Docker container:
    ```sh
    make rebuild
    ```
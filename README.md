# Selenium Login Automation

This project automates the login process to the `cesar.emineo-informatique.fr` website using Selenium WebDriver in Python. It uses environment variables to securely manage login credentials.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python packages:

    ```sh
    py -m pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your login credentials:

    ```dotenv
    LOGIN=your_username
    PASSWORD=your_password
    ```

## Usage

Run the `main.py` script to start the automation:

```sh
py main.py
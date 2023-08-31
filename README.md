# Goodreads Auto-Friend Adder

Automate the process of adding friends on Goodreads using Playwright and Python. This script logs into your Goodreads account, navigates to a friends list, and adds all friends on the list. It will continue to the next page and repeat the process until no more friends can be added.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x
- A Goodreads account

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/goodreads-auto-friend-adder.git
    cd goodreads-auto-friend-adder
    ```

2. **Install Python Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright and Browsers**

    ```bash
    npm install playwright
    ```

## Usage

1. **Set Environment Variables**

    Create a `.env` file in the root directory and add your Goodreads credentials:

    ```env
    GOODREADS_USERNAME=your_username
    GOODREADS_PASSWORD=your_password
    ```

2. **Run the Script**

    ```bash
    python add_friends.py
    ```

    The script will log into Goodreads, navigate to the friends list, and start adding friends. It will continue to the next page until no more friends can be added.

## Contributing

This is a private repo. Pull requests are not welcome. For major changes, contact the author.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
# Contributing to Kali Tool Atlas

I welcome contributions to the Kali Tool Atlas! Whether it's reporting a bug, suggesting a new feature, or submitting code, your help is greatly appreciated.

## How to Report Bugs

If you find a bug, please open an issue on GitHub. When reporting a bug, please include:
*   A clear and concise description of the bug.
*   Steps to reproduce the behavior.
*   Expected behavior.
*   Screenshots or error messages if applicable.
*   Your operating system and Python version.

## How to Suggest New Features

If you have an idea for a new feature or an improvement, please open an issue on GitHub. Describe your idea clearly and explain why you think it would be a valuable addition to the Kali Tool Atlas.

## How to Contribute Code

I follow a standard GitHub workflow for contributions:

1.  **Fork the Repository:** Start by forking the `Kbryaann/kali-tool-atlas` repository to your own GitHub account.
2.  **Clone Your Fork:** Clone your forked repository to your local machine.
    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/kali-tool-atlas.git
    cd kali-tool-atlas/project
    ```
3.  **Create a New Branch:** Create a new branch for your feature or bug fix.
    ```bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/your-bug-fix-name
    ```
4.  **Set up Development Environment:**
    *   Create and activate a virtual environment:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    *   Install dependencies:
        ```bash
        pip install rich
        ```
5.  **Make Your Changes:** Implement your feature or fix the bug.
    *   Ensure your code adheres to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines.
    *   Add comments where necessary to explain complex logic.
    *   Test your changes thoroughly.
6.  **Commit Your Changes:** Commit your changes with a clear and descriptive commit message.
    ```bash
    git add .
    git commit -m "feat: Add new feature X"
    # or
    git commit -m "fix: Resolve bug Y"
    ```
7.  **Push to Your Fork:** Push your new branch to your forked repository on GitHub.
    ```bash
    git push origin feature/your-feature-name
    ```
8.  **Open a Pull Request:** Go to the original `Kbryaann/kali-tool-atlas` repository on GitHub and open a Pull Request from your new branch.
    *   Provide a clear title and description for your Pull Request, explaining the changes you've made.

Thank you for your contributions!

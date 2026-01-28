# Kali Tool Atlas
#### Video Demo:  <URL HERE>
#### Description:
This is where you will write a detailed description of your project. Aim for around 750 words.

**What is Kali Tool Atlas?**
Explain the purpose of your tool. What problem does it solve? How does it help users?

**Features:**
List and describe the main features of your tool:
*   `list`: Lists all tools, grouped by category.
*   `search <query>`: Searches for tools by name or description.
*   `show <tool_name>`: Displays detailed information for a specific tool.
*   `add --name <name> --category <category> --description <description> --url <url>`: Adds a new tool to the Atlas.
*   `remove <tool_name>`: Removes a tool from the Atlas.
*   `edit <tool_name> [--name <new_name>] [--category <new_category>] [--description <new_description>] [--url <new_url>]`: Edits an existing tool's details.

**How to Run:**
Provide instructions on how to set up and run your project. Include steps for:
1.  Cloning the repository (once you set one up).
2.  Navigating to the `project` directory.
3.  Creating and activating the virtual environment.
4.  Installing dependencies (`pip install rich`).
5.  Running the `main.py` script with various commands (e.g., `python main.py list`).

**File Structure:**
Describe each file you've created and its purpose:
*   `project/main.py`: The main Python script containing all the CLI logic.
*   `project/tools.json`: The JSON file storing the tool data.
*   `project/.venv/`: The Python virtual environment for dependencies.

**Design Choices:**
Discuss any significant design decisions you made. For example:
*   Why did you choose Python?
*   Why did you choose JSON for data storage instead of a database? (Simplicity, no external dependencies for a CLI tool).
*   Why did you use `argparse` for command-line arguments?
*   Why did you use the `rich` library for output? How does it improve the user experience?
*   How did you handle case-insensitivity for tool names?
*   How did you ensure unique tool names?

**Future Improvements:**
What could be added or improved in the future?
*   More robust error handling.
*   Integration with external APIs to fetch tool information.
*   A graphical user interface (GUI).
*   More advanced search capabilities.

Remember to elaborate on each point to reach the desired word count and thoroughly explain your project.

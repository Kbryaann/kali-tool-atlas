# Kali Tool Atlas
#### Video Demo:  <URL HERE>
#### Description:
Kali Tool Atlas
1. Overall Description (Introduction)

Kali Tool Atlas is a command-line interface (CLI) application designed to help cybersecurity students and enthusiasts efficiently organize, discover, and reference tools within the Kali Linux ecosystem. Kali Linux contains hundreds of specialized tools, and keeping track of their names, purposes, and documentation can quickly become overwhelming, especially for learners.

I created this project to solve that problem by building a simple, structured, and searchable catalog that runs directly in the terminal. Instead of relying on memory, browser bookmarks, or repeatedly searching online, users can quickly look up tools by category or keyword and access official documentation links from one centralized place.

2. What is Kali Tool Atlas?

In cybersecurity, users often face several challenges:

Forgetting tool names

Not remembering what a tool does

Difficulty finding official documentation quickly

Constantly switching between the terminal and a web browser

Kali Tool Atlas addresses these issues by providing a local, searchable index of cybersecurity tools. The application allows users to list tools by category, search for tools using partial keywords, view detailed information for a specific tool, and manage their own personalized tool database.

The target audience for this tool includes:

Cybersecurity students

Beginners learning Kali Linux

Penetration testing learners

Anyone who wants a lightweight CLI reference for security tools

By reducing cognitive load and time spent searching for information, Kali Tool Atlas helps users focus more on learning and practical work.

3. Features
list

Displays all tools stored in the Atlas, grouped by category. This allows users to easily browse related tools and discover what is available within a specific domain, such as network scanning or web security.

Output is formatted using the rich library for readability.

Categories are clearly separated.

Usage:

python main.py list

search <query>

Searches for tools using a keyword. The search is:

Case-insensitive

Partial-match based

Applied to both tool names and descriptions

This is useful when the user remembers only part of a tool’s name or function.

Usage:

python main.py search scan

show <tool_name>

Displays detailed information about a specific tool, including:

Name

Category

Description

Official documentation or repository URL

Tool name matching is case-insensitive.

Usage:

python main.py show Nmap

add

Adds a new tool to the Atlas. This command requires all fields to be provided and prevents duplicate tool names to maintain data integrity.

Required fields:

Name

Category

Description

URL

Usage:

python main.py add --name "Nmap" \
                  --category "Network Scanning" \
                  --description "A powerful network scanning tool." \
                  --url "https://nmap.org"

remove <tool_name>

Removes an existing tool from the Atlas. If the specified tool does not exist, the program displays an error message instead of silently failing.

Usage:

python main.py remove Nmap

edit <tool_name>

Edits an existing tool’s information. This allows users to update fields such as the name, category, description, or URL without removing and re-adding the tool.

Usage:

python main.py edit Nmap --description "Updated description"

4. How to Run

Follow these steps to set up and run Kali Tool Atlas locally.

1. Clone the repository
git clone https://github.com/Kbryaann/kali-tool-atlas.git

2. Navigate to the project directory
cd kali-tool-atlas

3. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

4. Install dependencies
pip install rich

5. Run the application

Examples:

python main.py list
python main.py search web
python main.py show Nmap
python main.py add --name "ToolName" --category "Category" --description "Description" --url "URL"
python main.py remove ToolName
python main.py edit ToolName --category "New Category"

5. File Structure

The project consists of the following files:

main.py
The main application file. It handles command-line argument parsing using argparse, loads and saves tool data, and implements all commands (list, search, show, add, remove, edit). It also integrates the rich library for improved terminal output.

tools.json
A JSON file used as the persistent data store for all tools. Each tool entry includes its name, category, description, and URL.

.gitignore
Specifies files and directories (such as virtual environments and cache files) that should not be tracked by Git.

6. Design Choices
Why Python?

Python was chosen for its readability, simplicity, and strong standard library support. These qualities align well with CS50’s emphasis on clear, understandable code. Python also makes it easy to implement command-line tools, file I/O, and structured data handling.

Why JSON instead of a database?

For a small-scale CLI application, using a JSON file provides a lightweight and dependency-free solution. JSON is human-readable, easy to modify, and sufficient for storing structured tool data without the overhead of setting up a database system.

Why argparse?

The argparse module provides a clean and standardized way to handle command-line arguments and subcommands. It allows the application to behave like a professional CLI tool while also automatically generating help messages.

Why rich?

The rich library was used to improve terminal output readability. By formatting tables and headings, it makes browsing and searching tools easier and more pleasant for users.

Case-Insensitive Matching & Unique Names

Tool names are handled in a case-insensitive manner to reduce user error. Enforcing unique tool names prevents duplicates and ensures consistent behavior when searching, editing, or removing tools.

7. Future Improvements

While Kali Tool Atlas is fully functional, several enhancements could be added in the future:

Tag System: Allow tools to have multiple tags for more flexible categorization.

Fuzzy Search: Improve search results when users make typos or approximate queries.

Automatic Updates: Fetch tool information from official online sources to keep entries up to date.

Tool Installation/Execution Integration: Optionally integrate with system package managers to install or run tools directly, with clear warnings and user confirmation.

Conclusion

Kali Tool Atlas is a practical, educational CLI application that helps organize and manage cybersecurity tools in a structured way. This project demonstrates my understanding of Python, command-line application design, file-based data storage, and user-focused problem solving, while also reflecting my personal learning journey in cybersecurity.

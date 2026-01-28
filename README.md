# Kali Tool Atlas
#### Video Demo:  <URL HERE>

## Overall Description

Kali Tool Atlas is a command-line interface (CLI) application designed to help cybersecurity students and enthusiasts efficiently organize, discover, and reference tools within the Kali Linux ecosystem.

Kali Linux includes hundreds of specialized tools, which can make it difficult—especially for learners—to remember tool names, understand their purposes, or quickly find official documentation. This project centralizes that information into a single, searchable, and user-managed CLI catalog, allowing users to focus more on learning and practical work rather than searching.

## What is Kali Tool Atlas?

In the world of cybersecurity, users frequently face the following problems:

- Forgetting tool names

- Not knowing what a specific tool does

- Difficulty locating official documentation

- Constant context switching between the terminal and a web browser

Kali Tool Atlas solves these issues by providing a local, searchable index of tools that runs entirely in the terminal. Users can browse tools by category, search using keywords, view detailed information, and manage their own personalized list of cybersecurity tools.

### Target Audience

1.Cybersecurity students

2.Beginners learning Kali Linux

3.Penetration testing learners

4.Anyone who wants a lightweight CLI reference for security tools

## Features
### list

- Displays all tools grouped by category

- Makes it easy to browse related tools

- Output is formatted using the rich library for readability

*python main.py list*

### search <query>

- Searches both tool names and descriptions

- Case-insensitive

- Supports partial keyword matching

**python main.py search scan**

### show <tool_name>

Displays full details for a specific tool:

- Name

- Category

- Description

- Documentation URL

Tool name matching is case-insensitive

***python main.py show Nmap***

### add

- Adds a new tool to the Atlas

- Requires all fields to be provided

- Prevents duplicate tool names to maintain data integrity

*python main.py add --name "Nmap" \
                  --category "Network Scanning" \
                  --description "A powerful network scanning tool." \
                  --url "https://nmap.org"*

### remove <tool_name>

- Removes an existing tool from the Atlas

- Displays an error message if the tool does not exist

****python main.py remove Nmap****

### edit <tool_name>

- Updates an existing tool’s information

- Allows modification of one or more fields without re-adding the tool

**python main.py edit Nmap --description "Updated description"**

## How to Run

Follow the steps below to set up and run Kali Tool Atlas locally.

1. Clone the Repository
<span style="color:#1f6feb; font-weight:600;"> Clone the project from GitHub to your local machine: </span>
git clone https://github.com/Kbryaann/kali-tool-atlas.git

2. Navigate to the Project Directory
<span style="color:#1f6feb; font-weight:600;"> Change into the project folder: </span>
cd kali-tool-atlas

3. Create and Activate a Virtual Environment
<span style="color:#1f6feb; font-weight:600;"> Create a Python virtual environment: </span>
python3 -m venv .venv

<span style="color:#1f6feb; font-weight:600;"> Activate the virtual environment: </span>
source .venv/bin/activate

4. Install Dependencies
<span style="color:#1f6feb; font-weight:600;"> Install required Python libraries: </span>
pip install rich

5. Run the Application
<span style="color:#1f6feb; font-weight:600;"> Use the following commands to interact with Kali Tool Atlas: </span>
python main.py list
python main.py search web
python main.py show Nmap
python main.py add --name "ToolName" --category "Category" --description "Description" --url "URL"
python main.py remove ToolName
python main.py edit ToolName --category "New Category"

File Structure
kali-tool-atlas/
├── main.py
├── tools.json
├── .gitignore

File Descriptions

main.py
The core application file. Handles command-line argument parsing with argparse, loads and saves tool data, and implements all CLI commands. It also integrates the rich library for formatted terminal output.

tools.json
A JSON file used as persistent storage for tool data. Each entry includes a name, category, description, and documentation URL.

.gitignore
Prevents unnecessary files (such as virtual environments and cache files) from being tracked by Git.

Design Choices
Why Python?

Python was chosen for its readability, simplicity, and strong standard library support. These qualities align well with CS50’s emphasis on clean, understandable code and made it ideal for building a CLI application.

Why JSON Instead of a Database?

For a small-scale CLI project, JSON provides a lightweight, dependency-free storage solution. It is human-readable, easy to maintain, and sufficient for the scope of this application.

Why argparse?

The argparse module enables clean handling of commands and arguments while automatically generating helpful usage messages, making the tool intuitive and professional.

Why rich?

The rich library enhances the terminal experience by improving readability through formatted tables and styled output.

Case-Insensitive Matching & Unique Names

Case-insensitive matching reduces user error, while enforcing unique tool names ensures consistent behavior across all commands.

Future Improvements

Possible future enhancements include:

Tag-based categorization for more flexible organization

Fuzzy search to improve results when users make typos

Automatic updates from official online documentation sources

Optional tool installation or execution integration with explicit warnings and user confirmation

#*Conclusion*#

Kali Tool Atlas is an educational and practical CLI application that simplifies the discovery and management of cybersecurity tools. This project demonstrates effective use of Python, command-line design, structured data storage, and thoughtful user experience design, while reflecting my personal learning journey in cybersecurity.

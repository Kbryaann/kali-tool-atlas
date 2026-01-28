# Kali Tool Atlas
    2 #### Video Demo: <URL HERE>
    3 
    4 ## About Kali Tool Atlas
    5 
    6 The Kali Tool Atlas is a command-line interface (CLI) application designed to help cybersecurity students and enthusiasts efficiently organize,
      discover, and reference tools within the Kali Linux ecosystem.
    7 
    8 Kali Linux includes hundreds of specialized tools, which can make it difficult—especially for learners—to remember tool names, understand their
      purposes, or quickly find official documentation. This project centralizes that information into a single, searchable, and user-managed CLI
      catalog, allowing users to focus more on learning and practical work rather than constantly searching.
    9 
   10 The Atlas solves common problems such as:
   11 *   Forgetting tool names
   12 *   Not knowing what a specific tool does
   13 *   Difficulty locating official documentation
   14 *   Constant context switching between the terminal and a web browser
   15 
   16 By providing a local, searchable index that runs entirely in the terminal, users can browse tools by category, search using keywords, view
      detailed information, and manage their own personalized list of cybersecurity tools.
   17 
   18 ### Target Audience
   19 
   20 The Kali Tool Atlas is designed for:
   21 1.  Cybersecurity students
   22 2.  Beginners learning Kali Linux
   23 3.  Penetration testing learners
   24 4.  Anyone who wants a lightweight CLI reference for security tools
   25 
   26 ## Features
   27 
   28 The Kali Tool Atlas provides the following commands to manage and explore your tool collection:
   29 
   30 ### `list`
   31 
   32 Displays all tools grouped by category. The output is formatted using the `rich` library for enhanced readability, making it easy to browse
      related tools.
  python main.py list

   1 
   2 ### `search <query>`
   3 
   4 Searches for tools by matching keywords against both their names and descriptions. The search is case-insensitive and supports partial keyword
     matching.
  python main.py search scan

   1 
   2 ### `show <tool_name>`
   3 
   4 Displays comprehensive details for a specific tool, including its Name, Category, Description, and Documentation URL. Tool name matching is case
     -insensitive.
  python main.py show Nmap

   1 
   2 ### `add`
   3 
   4 Adds a new tool to the Atlas. This command requires all fields (`--name`, `--category`, `--description`, `--url`) to be provided and includes a
     check to prevent adding tools with duplicate names, ensuring data integrity.
  python main.py add --name "Nmap" \
                    --category "Network Scanning" \
                    --description "A powerful network scanning tool." \
                    --url "https://nmap.org"
   1 
   2 ### `remove <tool_name>`
   3 
   4 Removes an existing tool from the Atlas. If the specified tool does not exist, an informative error message is displayed.
  python main.py remove Nmap

   1 
   2 ### `edit <tool_name>`
   3 
   4 Updates an existing tool’s information. This command allows modification of one or more fields (`--name`, `--category`, `--description`, `--url`)
     without needing to re-add the entire tool.
  python main.py edit Nmap --description "Updated description for Nmap" --category "Network Reconnaissance"

   1 
   2 ## How to Run
   3 
   4 Follow the steps below to set up and run Kali Tool Atlas locally on your system.
   5 
   6 1.  **Clone the Repository**
   7     Clone the project from GitHub to your local machine:
      git clone https://github.com/Kbryaann/kali-tool-atlas.git

   1 
   2 2.  **Navigate to the Project Directory**
   3     Change your current directory to the project folder:
      cd kali-tool-atlas/project
   1 
   2 3.  **Create and Activate a Virtual Environment**
   3     Create a Python virtual environment to manage dependencies:
      python3 -m venv .venv
   1     Activate the virtual environment:
      source .venv/bin/activate  # On Linux/macOS
  .venv\Scripts\activate   # On Windows (Command Prompt)
  .venv\Scripts\Activate.ps1 # On Windows (PowerShell)
   1 
   2 4.  **Install Dependencies**
   3     Install the required Python libraries (e.g., `rich`) into your virtual environment:
      pip install rich

   1 
   2 5.  **Run the Application**
   3     You can now use the `python main.py` command followed by any of the available features:
      python main.py list
      python main.py search web
      python main.py show Nmap
      python main.py add --name "ToolName" --category "Category" --description "Description" --url "URL"
      python main.py remove ToolName
      python main.py edit ToolName --category "New Category"

    1 
    2 ## Project Structure
    3 
    4 The `kali-tool-atlas` project is organized as follows:
    5 
    6 ### File Descriptions
    7 
    8 *   **`main.py`**: This is the core Python script that orchestrates the entire application. It handles command-line argument parsing with
      `argparse`, loads and saves tool data, and implements all CLI commands (list, search, show, add, remove, edit). It also integrates the `rich`
      library for enhanced, formatted terminal output.
    9 *   **`tools.json`**: This JSON file serves as the persistent data store for all the tools in the Atlas. Each tool's information (name, category, 
      description, URL) is stored here in a structured format, allowing for easy reading and writing by the `main.py` script.
   10 *   **`.gitignore`**: This file instructs Git to ignore specific files and directories (such as the `.venv/` virtual environment and
      `__pycache__/` directories) from being tracked by version control, keeping the repository clean and focused on source code.
   11 *   **`.venv/`**: This directory contains the Python virtual environment for the project. It isolates the project's dependencies (like the `rich`
      library) from the system-wide Python installation, ensuring a clean and reproducible development environment.
   12 *   **`LICENSE`**: Specifies the open-source license (MIT) under which the project is distributed, outlining terms for use, modification, and
      distribution.
   13 *   **`CONTRIBUTING.md`**: Provides guidelines for individuals interested in contributing to the project, covering bug reporting, feature
      suggestions, and code contributions.
   14 *   **`CODE_OF_CONDUCT.md`**: Establishes behavioral expectations for all contributors and participants to foster a welcoming and inclusive
      community.
   15 
   16 ## Design Choices
   17 
   18 ### Why Python?
   19 
   20 Python was chosen for its readability, simplicity, and strong standard library support. These qualities align well with CS50’s emphasis on clean,
      understandable code and made it ideal for building a CLI application. Its extensive ecosystem also provided powerful libraries like `argparse` and
      `rich` that significantly enhanced development.
   21 
   22 ### Why JSON Instead of a Database?
   23 
   24 For a small-scale CLI project like the Kali Tool Atlas, using a JSON file (`tools.json`) for data storage offered several advantages over a
      traditional database. It eliminated the need for external database server dependencies, simplifying setup and deployment. JSON's human-readable 
      format also made it easy to inspect and manually edit the tool data if necessary. While a database might be more scalable for larger datasets, 
      JSON provided sufficient flexibility and performance for this project's scope, keeping the solution lightweight and self-contained.
   25 
   26 ### Why `argparse`?
   27 
   28 The `argparse` module was selected for handling command-line arguments due to its robustness and ease of use. It allows for defining subcommands (
      `list`, `search`, `add`, etc.) and their respective arguments, automatically generating helpful usage messages and error handling. This makes the
      tool intuitive for users and simplifies the parsing logic within the `main.py` script.
   29 
   30 ### Why `rich`?
   31 
   32 The `rich` library was integrated to significantly enhance the terminal user experience. It provides beautiful and readable output through
      features like colored text, panels, and columns. This transforms a standard text-based CLI into a more professional and engaging application,
      making information easier to digest and improving overall usability.
   33 
   34 ### Case-Insensitive Matching & Unique Names
   35 
   36 Implementing case-insensitive matching for tool names (in `search`, `show`, `remove`, `edit`) reduces user error and improves the tool's 
      flexibility. Simultaneously, enforcing unique tool names during the `add` and `edit` operations ensures data consistency and prevents ambiguity 
      across all commands, leading to a more reliable and predictable user experience.
   37 
   38 ## Future Improvements
   39 
   40 Possible future enhancements for the Kali Tool Atlas include:
   41 
   42 *   **Tag-based Categorization**: Implementing a more flexible tagging system to allow tools to belong to multiple categories or be filtered by
      specific tags.
   43 *   **Fuzzy Search**: Integrating fuzzy search capabilities to provide more forgiving search results, even when users make minor typos or partial
      entries.
   44 *   **Automatic Updates from Official Online Documentation**: Developing a feature to periodically fetch and update tool information
      (descriptions, URLs) from official online sources, keeping the Atlas current.
   45 *   **Optional Tool Installation or Execution Integration**: Exploring the possibility of adding commands to directly install or execute tools,
      with explicit warnings and user confirmation, to further streamline the workflow.
   46 
   47 ## Conclusion
   48 
   49 The Kali Tool Atlas is an educational and practical CLI application that simplifies the discovery and management of cybersecurity tools. This
      project demonstrates effective use of Python, command-line design, structured data storage, and thoughtful user experience design, while
      reflecting my personal learning journey in cybersecurity.


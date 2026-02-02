 # Kali Tool Atlas
     #### Video Demo: <URL HERE>
    
     ## About Kali Tool Atlas
    
     The Kali Tool Atlas is a command-line interface (CLI) application designed to help cybersecurity students and enthusiasts efficiently organize,
     discover, and reference tools within the Kali Linux ecosystem.
     
     Kali Linux includes hundreds of specialized tools, which can make it difficult—especially for learners—to remember tool names, understand their
     purposes, or quickly find official documentation. This project centralizes that information into a single, searchable, and user-managed CLI
     catalog, allowing users to focus more on learning and practical work rather than constantly searching.
     
    The Atlas solves common problems such as:
    *   Forgetting tool names
    *   Not knowing what a specific tool does
    *   Difficulty locating official documentation
    *   Constant context switching between the terminal and a web browser
    
    By providing a local, searchable index that runs entirely in the terminal, users can browse tools by category, search using keywords, view
      detailed information, and manage their own personalized list of cybersecurity tools.
    
    ### Target Audience
    
    The Kali Tool Atlas is designed for:
    1.  Cybersecurity students
    2.  Beginners learning Kali Linux
    3.  Penetration testing learners
    4.  Anyone who wants a lightweight CLI reference for security tools
    
    ## Features
    
    The Kali Tool Atlas provides the following commands to manage and explore your tool collection:
    
    ### `list`
    
    Displays all tools grouped by category. The output is formatted using the `rich` library for enhanced readability, making it easy to browse
    related tools.
  python main.py list

    
    ### `search <query>`
    
    Searches for tools by matching keywords against both their names and descriptions. The search is case-insensitive and supports partial keyword
    matching.
  python main.py search scan

    
    ### `show <tool_name>`
    
    Displays comprehensive details for a specific tool, including its Name, Category, Description, and Documentation URL. Tool name matching is case
    -insensitive.
  python main.py show Nmap

    
    ### `add`
    
    Adds a new tool to the Atlas. This command requires all fields (`--name`, `--category`, `--description`, `--url`) to be provided and includes a
    check to prevent adding tools with duplicate names, ensuring data integrity.
  python main.py add --name "Nmap" \
                    --category "Network Scanning" \
                    --description "A powerful network scanning tool." \
                    --url "https://nmap.org"
   
    ### `remove <tool_name>`
    
    Removes an existing tool from the Atlas. If the specified tool does not exist, an informative error message is displayed.
  python main.py remove Nmap

    
    ### `edit <tool_name>`
    
    Updates an existing tool’s information. This command allows modification of one or more fields (`--name`, `--category`, `--description`, `--url`)
    without needing to re-add the entire tool.
  python main.py edit Nmap --description "Updated description for Nmap" --category "Network Reconnaissance"

    
    ## How to Run
   
    Follow the steps below to set up and run Kali Tool Atlas locally on your system.
    
    1.**Clone the Repository**
      
      git clone https://github.com/Kbryaann/kali-tool-atlas.git

    2. **Navigate to the Project Directory**
       
       cd kali-tool-atlas/project
    
    3.  **Create and Activate a Virtual Environment**
        
       python3 -m venv .venv
        Activate the virtual environment:
        
       source .venv/bin/activate  # On Linux/macOS
  .venv\Scripts\activate   # On Windows (Command Prompt)
  .venv\Scripts\Activate.ps1 # On Windows (PowerShell)
    
    4.  **Install Dependencies**
       
      pip install rich
 
    5.  **Run the Application**
        You can now use the `python main.py` command followed by any of the available features:
      python main.py list
      python main.py search web
      python main.py show Nmap
      python main.py add --name "ToolName" --category "Category" 
      -- description "Description" --url "URL"
      python main.py remove ToolName
      python main.py edit ToolName --category "New Category"

    
    ## Project Structure
     
     The `kali-tool-atlas` project is organized as follows:
     
     ### File Descriptions
     
     *   **`main.py`**: This is the core Python script that orchestrates the entire application. It handles command-line argument parsing with
      `argparse`, loads and saves tool data, and implements all CLI commands (list, search, show, add, remove, edit). It also integrates the `rich`
      library for enhanced, formatted terminal output.
    *   **`tools.json`**: This JSON file serves as the persistent data store for all the tools in the Atlas. Each tool's information (name, category, 
      description, URL) is stored here in a structured format, allowing for easy reading and writing by the `main.py` script.
    *   **`.gitignore`**: This file instructs Git to ignore specific files and directories (such as the `.venv/` virtual environment and
      `__pycache__/` directories) from being tracked by version control, keeping the repository clean and focused on source code.
    *   **`.venv/`**: This directory contains the Python virtual environment for the project. It isolates the project's dependencies (like the `rich`
      library) from the system-wide Python installation, ensuring a clean and reproducible development environment.
    *   **`LICENSE`**: Specifies the open-source license (MIT) under which the project is distributed, outlining terms for use, modification, and
      distribution.
    *   **`CONTRIBUTING.md`**: Provides guidelines for individuals interested in contributing to the project, covering bug reporting, feature
      suggestions, and code contributions.
    *   **`CODE_OF_CONDUCT.md`**: Establishes behavioral expectations for all contributors and participants to foster a welcoming and inclusive
      community.
 
    ## Design Choices
    
    ### Why Python?
    
    Python was chosen for its readability, simplicity, and strong standard library support. These qualities align well with CS50’s emphasis on clean,
    understandable code and made it ideal for building a CLI application. Its extensive ecosystem also provided powerful libraries like `argparse` and
    `rich` that significantly enhanced development.
    
    ### Why JSON Instead of a Database?
    
    For a small-scale CLI project like the Kali Tool Atlas, using a JSON file (`tools.json`) for data storage offered several advantages over a
    traditional database. It eliminated the need for external database server dependencies, simplifying setup and deployment. JSON's human-readable 
    format also made it easy to inspect and manually edit the tool data if necessary. While a database might be more scalable for larger datasets, 
    JSON provided sufficient flexibility and performance for this project's scope, keeping the solution lightweight and self-contained.
    
    ### Why `argparse`?
    
    The `argparse` module was selected for handling command-line arguments due to its robustness and ease of use. It allows for defining subcommands (
    `list`, `search`, `add`, etc.) and their respective arguments, automatically generating helpful usage messages and error handling. This makes the
    tool intuitive for users and simplifies the parsing logic within the `main.py` script.
   
    ### Why `rich`?
    
    The `rich` library was integrated to significantly enhance the terminal user experience. It provides beautiful and readable output through
    features like colored text, panels, and columns. This transforms a standard text-based CLI into a more professional and engaging application,
    making information easier to digest and improving overall usability.
    
    ### Case-Insensitive Matching & Unique Names
    
    Implementing case-insensitive matching for tool names (in `search`, `show`, `remove`, `edit`) reduces user error and improves the tool's 
    flexibility. Simultaneously, enforcing unique tool names during the `add` and `edit` operations ensures data consistency and prevents ambiguity 
    across all commands, leading to a more reliable and predictable user experience.
    
    ## Future Improvements
    
    Possible future enhancements for the Kali Tool Atlas include:
    
    *   **Tag-based Categorization**: Implementing a more flexible tagging system to allow tools to belong to multiple categories or be filtered by
      specific tags.
    *   **Fuzzy Search**: Integrating fuzzy search capabilities to provide more forgiving search results, even when users make minor typos or partial
      entries.
    *   **Automatic Updates from Official Online Documentation**: Developing a feature to periodically fetch and update tool information
      (descriptions, URLs) from official online sources, keeping the Atlas current.
    *   **Optional Tool Installation or Execution Integration**: Exploring the possibility of adding commands to directly install or execute tools,
      with explicit warnings and user confirmation, to further streamline the workflow.
    
    ## Conclusion
   
    The Kali Tool Atlas is an educational and practical CLI application that simplifies the discovery and management of cybersecurity tools. This
    project demonstrates effective use of Python, command-line design, structured data storage, and thoughtful user experience design, while
    reflecting my personal learning journey in cybersecurity.

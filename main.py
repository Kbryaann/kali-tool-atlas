import json
import os
import argparse
from collections import defaultdict
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns

# Initialize Rich Console
console = Console()

# Define the absolute path to the tools.json file
TOOLS_FILE = os.path.join(os.path.dirname(__file__), 'tools.json')

def load_tools():
    """Loads tool data from the JSON file."""
    if not os.path.exists(TOOLS_FILE):
        console.print(f"[bold red]Error:[/bold red] {TOOLS_FILE} not found.")
        return []
    try:
        with open(TOOLS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        console.print(f"[bold red]Error:[/bold red] Could not decode JSON from {TOOLS_FILE}. Check file format.")
        return []
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred while loading tools:[/bold red] {e}")
        return []

def list_tools(tools):
    """Lists all tools, grouped by category."""
    if not tools:
        console.print("[yellow]No tools available in the Atlas.[/yellow]")
        return

    categorized_tools = defaultdict(list)
    for tool in tools:
        categorized_tools[tool.get('category', 'Uncategorized')].append(tool)

    for category, tool_list in sorted(categorized_tools.items()):
        console.print(Panel(f"[bold blue]{category}[/bold blue]", expand=False))
        tool_names = [Text(tool['name'], style="green") for tool in sorted(tool_list, key=lambda x: x['name'].lower())]
        console.print(Columns(tool_names, column_first=True, expand=True))
        console.print() # Add a newline for spacing

def search_tools(tools, query):
    """Searches for tools by name or description."""
    query_lower = query.lower()
    found_tools = []
    for tool in tools:
        if query_lower in tool['name'].lower() or query_lower in tool['description'].lower():
            found_tools.append(tool)

    if found_tools:
        console.print(Panel(f"[bold yellow]Search results for '{query}'[/bold yellow]", expand=False))
        for tool in found_tools:
            console.print(f"  [green]{tool['name']}[/green] ([cyan]{tool['category']}[/cyan])")
    else:
        console.print(f"[yellow]No tools found matching '{query}'.[/yellow]")

def show_tool_details(tools, tool_name):
    """Displays detailed information for a specific tool."""
    tool_name_lower = tool_name.lower()
    found_tool = None
    for tool in tools:
        if tool['name'].lower() == tool_name_lower:
            found_tool = tool
            break

    if found_tool:
        details = Text()
        details.append(f"Name: [bold green]{found_tool['name']}[/bold green]\n")
        details.append(f"Category: [cyan]{found_tool['category']}[/cyan]\n")
        details.append(f"Description: [white]{found_tool['description']}[/white]\n")
        details.append(f"URL: [link={found_tool['url']}]{found_tool['url']}[/link]")
        console.print(Panel(details, title=f"[bold magenta]Details for {found_tool['name']}[/bold magenta]", border_style="magenta"))
    else:
        console.print(f"[bold red]Tool '{tool_name}' not found in the Atlas.[/bold red]")

import json
import os
import argparse
from collections import defaultdict
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns

# Initialize Rich Console
console = Console()

# Define the absolute path to the tools.json file
TOOLS_FILE = os.path.join(os.path.dirname(__file__), 'tools.json')

def load_tools():
    """Loads tool data from the JSON file."""
    if not os.path.exists(TOOLS_FILE):
        console.print(f"[bold red]Error:[/bold red] {TOOLS_FILE} not found.")
        return []
    try:
        with open(TOOLS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        console.print(f"[bold red]Error:[/bold red] Could not decode JSON from {TOOLS_FILE}. Check file format.")
        return []
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred while loading tools:[/bold red] {e}")
        return []

def save_tools(tools):
    """Saves tool data to the JSON file."""
    try:
        with open(TOOLS_FILE, 'w') as f:
            json.dump(tools, f, indent=2)
        return True
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Could not save tools to {TOOLS_FILE}: {e}")
        return False

def list_tools(tools):
    """Lists all tools, grouped by category."""
    if not tools:
        console.print("[yellow]No tools available in the Atlas.[/yellow]")
        return

    categorized_tools = defaultdict(list)
    for tool in tools:
        categorized_tools[tool.get('category', 'Uncategorized')].append(tool)

    for category, tool_list in sorted(categorized_tools.items()):
        console.print(Panel(f"[bold blue]{category}[/bold blue]", expand=False))
        tool_names = [Text(tool['name'], style="green") for tool in sorted(tool_list, key=lambda x: x['name'].lower())]
        console.print(Columns(tool_names, column_first=True, expand=True))
        console.print() # Add a newline for spacing

def search_tools(tools, query):
    """Searches for tools by name or description."""
    query_lower = query.lower()
    found_tools = []
    for tool in tools:
        if query_lower in tool['name'].lower() or query_lower in tool['description'].lower():
            found_tools.append(tool)

    if found_tools:
        console.print(Panel(f"[bold yellow]Search results for '{query}'[/bold yellow]", expand=False))
        for tool in found_tools:
            console.print(f"  [green]{tool['name']}[/green] ([cyan]{tool['category']}[/cyan])")
    else:
        console.print(f"[yellow]No tools found matching '{query}'.[/yellow]")

def show_tool_details(tools, tool_name):
    """Displays detailed information for a specific tool."""
    tool_name_lower = tool_name.lower()
    found_tool = None
    for tool in tools:
        if tool['name'].lower() == tool_name_lower:
            found_tool = tool
            break

    if found_tool:
        details = Text()
        details.append(f"Name: [bold green]{found_tool['name']}[/bold green]\n")
        details.append(f"Category: [cyan]{found_tool['category']}[/cyan]\n")
        details.append(f"Description: [white]{found_tool['description']}[/white]\n")
        details.append(f"URL: [link={found_tool['url']}]{found_tool['url']}[/link]")
        console.print(Panel(details, title=f"[bold magenta]Details for {found_tool['name']}[/bold magenta]", border_style="magenta"))
    else:
        console.print(f"[bold red]Tool '{tool_name}' not found in the Atlas.[/bold red]")

def add_tool(tools, name, category, description, url):
    """Adds a new tool to the Atlas."""
    # Check for duplicate tool names (case-insensitive)
    if any(tool['name'].lower() == name.lower() for tool in tools):
        console.print(f"[bold red]Error:[/bold red] Tool with name '{name}' already exists.")
        return

    new_tool = {
        "name": name,
        "category": category,
        "description": description,
        "url": url
    }
    tools.append(new_tool)
    if save_tools(tools):
        console.print(f"[bold green]Tool '{name}' added successfully![/bold green]")
    else:
        console.print(f"[bold red]Failed to add tool '{name}'.[/bold red]")

def remove_tool(tools, tool_name):
    """Removes a tool from the Atlas."""
    tool_name_lower = tool_name.lower()
    initial_tool_count = len(tools)
    tools[:] = [tool for tool in tools if tool['name'].lower() != tool_name_lower]

    if len(tools) < initial_tool_count:
        if save_tools(tools):
            console.print(f"[bold green]Tool '{tool_name}' removed successfully![/bold green]")
        else:
            console.print(f"[bold red]Failed to remove tool '{tool_name}'.[/bold red]")
    else:
        console.print(f"[bold red]Tool '{tool_name}' not found in the Atlas.[/bold red]")

def edit_tool(tools, old_name, new_name=None, category=None, description=None, url=None):
    """Edits an existing tool in the Atlas."""
    tool_found = False
    for tool in tools:
        if tool['name'].lower() == old_name.lower():
            tool_found = True
            # Check for duplicate new name if name is being changed
            if new_name and new_name.lower() != old_name.lower() and \
               any(t['name'].lower() == new_name.lower() for t in tools if t is not tool):
                console.print(f"[bold red]Error:[/bold red] New name '{new_name}' already exists for another tool.")
                return

            if new_name:
                tool['name'] = new_name
            if category:
                tool['category'] = category
            if description:
                tool['description'] = description
            if url:
                tool['url'] = url

            if save_tools(tools):
                console.print(f"[bold green]Tool '{old_name}' updated successfully![/bold green]")
                if new_name and new_name.lower() != old_name.lower():
                    console.print(f"[bold green]Tool name changed to '{new_name}'.[/bold green]")
            else:
                console.print(f"[bold red]Failed to update tool '{old_name}'.[/bold red]")
            return

    if not tool_found:
        console.print(f"[bold red]Tool '{old_name}' not found in the Atlas.[/bold red]")


def main():
    parser = argparse.ArgumentParser(
        description="Kali Tool Atlas: A categorized index of security tools.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tools, grouped by category.')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search for tools by name or description.')
    search_parser.add_argument('query', type=str, help='The search query.')

    # Show command
    show_parser = subparsers.add_parser('show', help='Show detailed information for a specific tool.')
    show_parser.add_argument('tool_name', type=str, help='The name of the tool to show details for.')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new tool to the Atlas.')
    add_parser.add_argument('--name', required=True, help='The name of the tool.')
    add_parser.add_argument('--category', required=True, help='The category of the tool.')
    add_parser.add_argument('--description', required=True, help='A brief description of the tool.')
    add_parser.add_argument('--url', required=True, help='The URL for the tool (e.g., GitHub repo, official website).')

    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a tool from the Atlas.')
    remove_parser.add_argument('tool_name', type=str, help='The name of the tool to remove.')

    # Edit command
    edit_parser = subparsers.add_parser('edit', help='Edit an existing tool in the Atlas.')
    edit_parser.add_argument('tool_name', type=str, help='The name of the tool to edit.')
    edit_parser.add_argument('--name', help='New name for the tool.')
    edit_parser.add_argument('--category', help='New category for the tool.')
    edit_parser.add_argument('--description', help='New description for the tool.')
    edit_parser.add_argument('--url', help='New URL for the tool.')


    args = parser.parse_args()

    tools = load_tools()
    if tools is None: # Handle case where load_tools returns None due to error
        return

    if args.command == 'list':
        list_tools(tools)
    elif args.command == 'search':
        search_tools(tools, args.query)
    elif args.command == 'show':
        show_tool_details(tools, args.tool_name)
    elif args.command == 'add':
        add_tool(tools, args.name, args.category, args.description, args.url)
    elif args.command == 'remove':
        remove_tool(tools, args.tool_name)
    elif args.command == 'edit':
        # Ensure at least one field is provided for editing
        if not any([args.name, args.category, args.description, args.url]):
            console.print("[bold red]Error:[/bold red] At least one field (--name, --category, --description, --url) must be provided to edit a tool.")
            edit_parser.print_help()
            return
        edit_tool(tools, args.tool_name, args.name, args.category, args.description, args.url)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


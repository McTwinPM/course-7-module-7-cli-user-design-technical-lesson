# Technical Lesson: CLI Structure & User-Focused Design

## Learning Goals

- Use `argparse` to define structured CLI commands and subcommands.
- Create user-friendly interfaces with descriptive help messages.
- Validate user input and handle errors gracefully.
- Group related functionality using subparsers for modular CLI design.

---

## Introduction

Command-line tools are powerful for automation and backend tasks. In this lesson, you'll learn how to build structured, user-friendly CLIs in Python using the `argparse` module.

You'll build a small task manager tool that supports:

- Commands like `add` and `list`
- Helpful usage messages
- Graceful handling of missing or invalid input

---

## Project Setup

### 1. Clone the Repository

```bash
git clone <repo-url>
cd course-7-module-5-cli-structure-technical-lesson
```

### 2. Install Dependencies

**Using Pipenv:**
```bash
pipenv install
pipenv shell
```

---

## Running the CLI

You can run the CLI using:

```bash
python generate_cli.py
```

Examples:

```bash
python generate_cli.py --help
python generate_cli.py add "Finish the README"
python generate_cli.py list
```

---

## Code Structure

```
.
├── generate_cli.py           # Entry point for the CLI
├── lib/
│   ├── __init__.py
│   └── cli_tool.py           # Contains argparse logic and command handlers
├── Pipfile
├── .gitignore
├── README.md
```

---

## Best Practices for CLI Design

- Use `argparse`'s `description` and `help` arguments for better UX
- Organize subcommands with `add_subparsers()`
- Separate CLI logic from business logic (e.g., use `lib/`)
- Use `if __name__ == "__main__":` in your entry point
- Write testable, modular code with good feedback for invalid input

---

## Conclusion

By the end of this lesson, you will know how to:

- Build a modular CLI using `argparse`
- Provide intuitive help messages and input validation
- Create clear command groups and handler functions
- Structure CLI tools that are easy to maintain and scale

These skills are essential for building professional-grade tools that users can depend on from the terminal.

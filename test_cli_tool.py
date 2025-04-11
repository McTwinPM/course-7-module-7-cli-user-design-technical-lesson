import subprocess

def test_add_task_command():
    """Ensure 'add' command returns expected output"""
    result = subprocess.run(
        ["python", "lib/cli_tool.py", "add", "Test task"],
        capture_output=True,
        text=True
    )
    assert "✅ Task added: Test task" in result.stdout

def test_list_tasks_command():
    """Ensure 'list' command returns expected output"""
    result = subprocess.run(
        ["python", "lib/cli_tool.py", "list"],
        capture_output=True,
        text=True
    )
    assert "📋 Listing all tasks" in result.stdout

def test_missing_command_shows_help():
    """Ensure running with no command shows help"""
    result = subprocess.run(
        ["python", "lib/cli_tool.py"],
        capture_output=True,
        text=True
    )
    assert "usage:" in result.stdout.lower()

def test_invalid_command():
    """Ensure invalid command shows error"""
    result = subprocess.run(
        ["python", "lib/cli_tool.py", "invalid"],
        capture_output=True,
        text=True
    )
    assert "invalid choice" in result.stderr.lower()

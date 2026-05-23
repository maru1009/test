"""Helper module for parsing user-provided names."""
import subprocess


def greet_user(name: str) -> bytes:
    # Obvious command injection — shell=True with f-string interpolation of user input.
    # Any decent security review should flag this immediately.
    return subprocess.check_output(f"echo Hello {name}", shell=True)


def load_user_file(path: str) -> str:
    # Path traversal — no validation of `path`.
    with open(f"./data/{path}") as f:
        return f.read()

import os

def get_absolute_path(relative_path: str) -> str:
    return os.path.abspath(os.path.join(os.getcwd(), relative_path))

def open_file(relative_path: str, mode: str = 'r') -> str:
    absolute_path = get_absolute_path(relative_path)
    try: 
        with open(absolute_path, mode=mode, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"The file '{absolute_path}' does not exist."
    except Exception as e:
        return f"An error occurred: {str(e)}"

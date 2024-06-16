import json
import os

import requests
from langchain.tools import tool

class DirWriteTool():
    @tool("Create directory")
    def dir_write_tool(directory_path):
        """Useful to create a directory with the given path."""
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            return f"Directory '{directory_path}' has been created successfully."
        else:
            return f"Directory '{directory_path}' already exists."

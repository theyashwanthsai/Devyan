import json
import os

import requests
from langchain.tools import tool

class FileWriteTool():
    @tool("Write file")
    def file_write_tool(filename, content):
        """Useful to write content to a file with the given filename."""
        try:
            with open(filename, 'w') as file:
                file.write(content)
            return f"File '{filename}' has been written successfully."
        except Exception as e:
            return f"Failed to write file '{filename}': {e}"
        return f"File '{filename}' has been written successfully."

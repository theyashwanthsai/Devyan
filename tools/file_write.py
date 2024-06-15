import json
import os

import requests
from langchain.tools import tool

class FileWriteTool():
    @tool("Write file")
    def file_write_tool(filename, content):
        """Useful to write content to a file with the given filename."""
        with open(filename, 'w') as file:
            file.write(content)
        return f"File '{filename}' has been written successfully."

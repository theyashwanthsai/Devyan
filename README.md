
# Devyan
## Overview

**Devyan** is an AI-powered software development assistant that orchestrates a team of agents to solve programming tasks. It uses OpenAI's GPT-based agents to perform various roles such as architecture design, implementation, testing, and reviewing.


![Video Description](gif.gif)
## Features

- **Architect Agent**: Designs the architecture of the solution based on the user input.
- **Programmer Agent**: Implements the solution as per the architecture design.
- **Tester Agent**: Tests the implemented solution to ensure it meets the requirements and is free of bugs.
- **Reviewer Agent**: Reviews the architecture, implementation, and test results to provide a comprehensive analysis.
![img](architecture.png)


## Requirements

- Python 3.7+
- `requests` library
- `langchain` library
- `python-decouple` library
- `crewai` library
- OpenAI API Key
- Milvus vector database
  

## Using Vector Database

This project uses Milvus as a vector database to store and search for relevant code snippets based on the user's query. The `MilvusClient` class handles the connection and operations with the Milvus server.

### Setting up Milvus

1. Install Milvus:

    ```sh
    pip install pymilvus
    ```

2. Start Milvus server:
    Follow the [Milvus installation guide](https://milvus.io/docs/install_standalone-docker.md) to set up and start the Milvus server.

3. Configure the connection:
    The `MilvusClient` class in `milvus_client.py` connects to the Milvus server running on `localhost` at port `19530` by default. You can change these settings in the `MilvusClient` class constructor.

### Example Usage

The `CustomCrew` class in `main.py` uses the `MilvusClient` to query for relevant code snippets based on the user's input. The retrieved code snippets are then used by various agents to perform their tasks.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/devain.git
    cd devain
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    SERPER_API_KEY=your_serper_api_key_here
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. Follow the prompts:
    ```text
    ## Welcome to Devain##
    -------------------------------
    What problem do you want us to solve?
    ```

3. Enter the problem you want Devain to solve, and let the agents handle the rest.

## Project Structure

```plaintext
devain/
│
│ 
├── tools/
│   ├── __init__.py
│   ├── file_write.py
│   └── directory_write.py
│
├── agents.py
│
├── tasks.py
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature``).
5. Open a pull request.

## Todo
- [x] Create Custom tool to write file
- [x] Create Custom tool to create directory
- [x] Change prompts in tasks, make it more detialed and clear
- [ ] Use pytoml
- [ ] Add Agent Logs
- [ ] Stackoverflow tool
- [ ] Code Execution
- [ ] Develop on existing codebase instead of generating new code every time


[![Star History Chart](https://api.star-history.com/svg?repos=theyashwanthsai/Devyan&type=Date)](https://star-history.com/#theyashwanthsai/Devyan&Date)

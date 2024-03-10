# Labelbox Python SDK
[![Release Notes](https://img.shields.io/github/release/labelbox/labelbox-python)](https://github.com/Labelbox/labelbox-python/releases)
[![CI](https://github.com/labelbox/labelbox-python/actions/workflows/python-package.yml/badge.svg)](https://github.com/labelbox/labelbox-python/actions)
[![Downloads](https://pepy.tech/badge/labelbox)](https://pepy.tech/project/labelbox)
[![Dependency Status](https://img.shields.io/librariesio/github/labelbox/labelbox-python)](https://libraries.io/github/labelbox/labelbox-python)
[![Open Issues](https://img.shields.io/github/issues-raw/labelbox/labelbox-python)](https://github.com/labelbox/labelbox-python/issues)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Twitter Follow](https://img.shields.io/twitter/follow/labelbox.svg?style=social&label=Follow)](https://twitter.com/labelbox)
[![LinkedIn Follow](https://img.shields.io/badge/Follow-LinkedIn-blue.svg?style=flat&logo=linkedin)](https://www.linkedin.com/company/labelbox/)


Labelbox is a cloud-based data-centric AI platform designed to help teams create high-quality training data for their AI models. It provides a suite of tools and features that streamline the process of data curation, labeling, model output evaluation for computer vision and large language models. Visit [Labelbox](http://labelbox.com/) for more information.


The Python SDK provides a convenient way to interact with Labelbox programmatically, offering advantages over REST or GraphQL APIs:

* **Simplified interactions:** The SDK abstracts away the complexities of API calls, making it easier to work with Labelbox.
* **Object-oriented approach:** The SDK provides an object-oriented interface, allowing you to interact with Labelbox entities (projects, datasets, labels, etc.) as Python objects.
* **Extensibility:** The SDK can be extended to support custom data formats and operations.

# Table of Contents

### Table of Contents
- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Building and installing locally](#building-and-installing-locally)
        - [Prerequisites](#prerequisites)
        - [Steps for Local Installation](#steps-for-local-installation)
- [Code Architecture](#code-architecture)
- [Contribution Guidelines](#contribution-guidelines)
- [Develop with AI Assistance](#develop-with-ai-assistance)
   - [Use the Codebase as Context for Large Language Models](#use-the-codebase-as-context-for-large-language-models)
   - [Ask Google Gemini to write a method](#ask-google-gemini-to-get-started)
- [Documentation](#documentation)
    - [Official Documentation](#official-documentation)
    - [Notebook Examples](#notebook-examples)
    - [API Reference](#api-reference)


## Installation
![Supported python versions](https://img.shields.io/badge/python-3.7%20|%203.8%20|%203.9%20|%203.10-blue.svg)

Welcome to the quick start guide for integrating Labelbox into your Python projects. Whether you're looking to incorporate advanced data labeling into your workflow or simply explore the capabilities of the Labelbox Python SDK, this guide will walk you through the two main methods of setting up Labelbox in your environment: via a package manager and by building it locally.

### Install using pip

To get started with the least amount of hassle, follow these simple steps to install the Labelbox Python SDK using pip, Python's package manager.

1. **Ensure pip is installed:** First, make sure you have `pip` installed on your system. It's the tool we'll use to install the SDK.
   
2. **Sign up for Labelbox:** If you haven't already, create a free account at [Labelbox](http://app.labelbox.com/) to access its features.

3. **Generate your API key:** Log into Labelbox and navigate to [Account > API Keys](https://docs.labelbox.com/docs/create-an-api-key) to generate an API key. You'll need this for programmatic access to Labelbox.

4. **Install the SDK:** Open your terminal or command prompt and run the following command to install the Labelbox Python SDK:
   
   ```bash
   pip install labelbox
   ```

5. **Install optional dependencies:** For enhanced functionality, such as data processing, you can install additional dependencies with:
   
   ```bash
   pip install "labelbox[data]"
   ```

   This includes essential libraries like Shapely, GeoJSON, NumPy, Pillow, and OpenCV-Python, enabling you to handle a wide range of data types and perform complex operations.

### Building and installing locally

For those who prefer or require a more hands-on approach, such as contributing to the SDK or integrating it into a complex project, building the SDK locally is the way to go.


#### Steps for local installation

1. **Clone the SDK repository:** First, clone the Labelbox SDK repository from GitHub to your local machine.

2. **Install required dependencies:** To ensure all dependencies are met, run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install the SDK locally:** Navigate to the root directory of the cloned repository and run:

   ```bash
   pip install -e .
   ```

   For additional data processing capabilities, remember to install the `data` extra as mentioned in the easy installation section.


## Code architecture
The Labelbox Python SDK is designed to provide a clean and intuitive interface for interacting with the Labelbox API. It primarily uses GraphQL for communication, with some REST API calls for specific functionalities. The SDK wraps the GraphQL API calls and provides object-oriented representations of Labelbox entities like projects, datasets, and labels. This allows developers to interact with Labelbox in a more Pythonic way, making code easier to read and maintain.

Key files and classes include:

- **`labelbox/client.py`:** Contains the `Client` class, which provides methods for interacting with the Labelbox API.
- **`labelbox/orm/model.py`:** Defines the data model for Labelbox entities like projects, datasets, and labels.
- **`labelbox/schema/*.py`:** Contains classes representing specific Labelbox entities and their attributes.
- **`labelbox/data/annotation_types/*.py`:** Defines classes for different annotation types, such as bounding boxes, polygons, and classifications.
- **`labelbox/data/serialization/*.py`:** Provides converters for different data formats, including NDJSON and Labelbox v1 JSON.

The SDK wraps the GraphQL APIs and provides a Pythonic interface for interacting with Labelbox.

## Contribution guidelines
We encourage developers to contribute to the Labelbox Python SDK and help improve its functionality and usability. Please refer to the `CONTRIB.md` file in the root folder of the repository for detailed information on how to contribute.

## Develop with AI assistance
### Use the codebase as context for large language models
Using the [GPT repository loader](https://github.com/mpoon/gpt-repository-loader), we have created `lbx_prompt.txt` that contains data from all `.py` and `.md` files. The file has about 730k tokens. We recommend using Gemini 1.5 Pro with 1 million context length window.

### Ask Google Gemini to get started
We asked Gemini about how to add a data format converter that takes in chat logs and imports as a chat (conversational) datarow in Labelbox. Here's the response using `lbx_prompt.txt` as context. Here's how you can add a method called `my_new_method` to the Labelbox Python SDK that converts chat logs into Labelbox conversational datarow format:

**1. Location:**

The method should be placed in the `labelbox/client.py` file within the `Client` class. This will allow you to access it using `client.utilities.my_new_method(params)`.

**2. Code:**

Here's the code for the `my_new_method` function:

```python
def my_new_method(self, chat_logs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Converts chat logs into Labelbox conversational datarow format.

    Args:
        chat_logs: A list of dictionaries representing chat messages. Each dictionary should have the following keys:
            - messageId: Unique identifier for the message.
            - timestampUsec: Timestamp of the message in microseconds.
            - content: The text content of the message.
            - user: A dictionary containing information about the user who sent the message, including:
                - userId: Unique identifier for the user.
                - name: Name of the user.
            - align: (Optional) "left" or "right" to indicate the alignment of the message. Defaults to "left".
            - canLabel: (Optional) Boolean indicating if the message can be labeled. Defaults to True.

    Returns:
        A list of dictionaries in Labelbox conversational datarow format.
    """

    datarows = []
    for chat_log in chat_logs:
        datarow = {
            "row_data": {
                "messages": [chat_log],
                "version": 1,
                "type": "application/vnd.labelbox.conversational"
            }
        }
        datarows.append(datarow)
    return datarows
```

**3. Explanation:**

This method takes a list of chat logs as input, where each chat log is represented as a dictionary with specific keys. The method then iterates through each chat log and creates a dictionary in Labelbox conversational datarow format. This format includes a `row_data` key with a nested dictionary containing the chat messages, version, and type information. Finally, the method returns a list of these datarow dictionaries.

**4. Usage:**

After adding the `my_new_method` function to the `Client` class, you can use it as follows:

```python
client = Client(api_key="YOUR_API_KEY")

# Prepare your chat logs as a list of dictionaries
chat_logs = [
    {
        "messageId": "message1",
        "timestampUsec": 1669000000,
        "content": "Hello, how are you?",
        "user": {"userId": "user1", "name": "John Doe"},
    },
    # ... more chat logs ...
]

# Convert chat logs to Labelbox format
datarows = client.utilities.my_new_method(chat_logs)

# Create data rows in a dataset
dataset = client.create_dataset(name="Chat Logs Dataset")
dataset.create_data_rows(datarows)
```

This will create data rows in the specified dataset, with each data row containing the information from a single chat log in the Labelbox conversational format. 

**5. Update README:**

Remember to update the README file to reflect the addition of the new method and provide a brief description of its functionality and usage.

## Documentation
The Labelbox Python SDK is well-documented to help developers get started quickly and use the SDK effectively. Here are some resources:

- **Official documentation:** https://docs.labelbox.com/docs/overview
- **Notebook examples:** https://github.com/Labelbox/labelbox-python/tree/master/examples
- **API reference:** https://labelbox-python.readthedocs.io/en/latest/

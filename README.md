BnB Clone Command Line Interface
--------------------------------

Welcome to the AirBnB clone project! This Command Line Interface (CLI) serves as the first step towards building a full web application, mimicking the functionality of AirBnB.

Background
----------

Before diving into the project, make sure to read the AirBnB concept page (**refer to AirBnB documentation for details**). This project aims to achieve several objectives, including:

*   Creating a parent class (BaseModel) to handle instance initialization, serialization, and deserialization.
    
*   Implementing a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
    
*   Defining classes for AirBnB objects such as User, State, City, and Place, which inherit from BaseModel.
    
*   Developing the first abstracted storage engine for the project: File storage.
    
*   Writing unit tests to validate all classes and storage engine functionalities.
    

Command Interpreter
-------------------

The CLI allows users to manage AirBnB objects through various commands:

*   create : Create a new instance of the specified class.
    
*   show : Show details of a specific instance.
    
*   destroy : Delete a specific instance.
    
*   all \[\]: List all instances of the specified class, or all instances if no class is specified.
    
*   update "": Update the value of a specific attribute of an instance.
    
*   quit or EOF: Exit the CLI.
    

File Storage
------------

The CLI utilizes a FileStorage class to serialize and deserialize instances to and from a JSON file (file.json). This ensures that the instances persist across sessions.

Requirements
------------

### Python Scripts

*   Python version: 3.x
    
*   The first line of all scripts should be #!/usr/bin/python3.
    
*   All files should be executable.
    
*   Use pycodestyle for code styling.
    
*   Include a README.md file at the root of the project folder.
    

### Python Unit Tests

*   Use the unittest module for writing tests.
    
*   All test files should be inside a folder named tests.
    
*   Test files and folders should start with test\_.
    
*   Tests can be executed using python3 -m unittest discover tests.
    

Contributing
------------

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please create a new issue or pull request.

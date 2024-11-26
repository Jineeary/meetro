Contribution Guidelines
========================

We welcome contributions to this project! This page outlines how to contribute to the **Meetro** project. This document outlines the process and guidelines for contributing, including coding standards and submission procedures.

1. Getting Started
------------------

Before contributing, please ensure you:

1. Fork the repository to your own GitHub account.
2. Clone the repository to your local machine:

.. code-block:: bash

   git clone https://github.com/<your-username>/<repository-name>.git

3. Install the required dependencies as specified in the `README` file or `requirements.txt`.

2. Coding Standards
-------------------

To maintain consistency and readability across the project, follow these coding standards:

- **Code Style**: Adhere to the [PEP 8](https://peps.python.org/pep-0008/) guidelines for Python code.
  - Use 4 spaces for indentation.
  - Limit lines to 79 characters.
- **Variable Naming**:
  - Use `snake_case` for variables and functions.
  - Use `PascalCase` for class names.
- **Documentation**:
  - Write clear docstrings for all functions and classes using the Google style guide.
  - Include inline comments where necessary.

**Example Function:**

.. code-block:: python

   def calculate_sum(a: int, b: int) -> int:
       """
       Calculates the sum of two numbers.

       Args:
           a (int): The first number.
           b (int): The second number.

       Returns:
           int: The sum of the two numbers.
       """
       return a + b

- **Testing**:
  - Include unit tests for all new functionality.
  - Use the `pytest` framework for testing.
  - Place tests in the `tests/` directory.

3. Step to Contribute
------------------------------

Follow these steps to submit your contribution:

1. **Create a Feature Branch**  
   - Create a new branch for your changes:
   
   .. code-block:: bash

      git checkout -b feature/<your-feature-name>

2. **Make Your Changes**  
   - Ensure your changes adhere to the coding standards outlined above.

3. **Run Tests**  
   - Run the existing tests and ensure all pass:
   
   .. code-block:: bash

      pytest

4. **Commit Your Changes**  
   - Use meaningful commit messages:
   
   .. code-block:: bash

      git commit -m "Add feature to calculate sum"

5. **Push Your Branch**  
   - Push your branch to your forked repository:
   
   .. code-block:: bash

      git push origin feature/<your-feature-name>

6. **Open a Pull Request**  
   - Go to the original repository on GitHub.
   - Open a Pull Request (PR) from your feature branch.
   - Provide a clear and concise description of your changes.

4. Reviewing and Merging Changes
---------------------------------

- A project maintainer will review your PR.
- Address any feedback promptly.
- Once approved, your changes will be merged into the main branch.

5. Code of Conduct
------------------

Please adhere to the project's Code of Conduct. Be respectful and constructive in all interactions.

6. Additional Resources
-----------------------

- [PEP 8 Python Style Guide](https://peps.python.org/pep-0008/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)


Thank You for Contributing!


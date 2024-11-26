Configuration Guide
===================

This document provides information about the project's configuration. It includes details on configuration options, default settings, and customization methods.

1. Introduction
---------------

- This guide explains how to configure and set up the project.
- It provides information to enable or customize various features of the project.

2. Installation and Initial Setup
---------------------------------

- Follow these steps to set up the project configuration:

**1. Install Required Dependencies**

.. code-block:: bash

   pip install -r requirements.txt

**2. Create Configuration Files**

- Example: Generate a `.env` or `config.yaml` file.
- Copy the template file (e.g., `.env.template`) and use it to create the environment variable file.

**3. Verify Default Settings**

- Test the initial setup to ensure proper configuration:

.. code-block:: bash

   python manage.py check_config

3. Configuration File Structure
-------------------------------

- Describes the location and structure of the configuration files.

**Example: YAML File Structure**

.. code-block:: yaml

   database:
     host: localhost
     port: 5432
     user: admin
     password: secret
   app:
     debug: true
     log_level: info

**Main Configuration Files**

1. **`config/settings.py`**  
   - Python-based configuration file.
2. **`.env`**  
   - Environment variable file.

4. Environment Variables
------------------------

- Key environment variables used in the project and their roles:

+-------------------+--------------------------------------+---------------------+
| Variable Name     | Description                          | Example             |
+===================+======================================+=====================+
| `DATABASE_URL`    | Database connection URL             | `postgres://...`    |
+-------------------+--------------------------------------+---------------------+
| `SECRET_KEY`      | Application security key            | `random_key_value`  |
+-------------------+--------------------------------------+---------------------+
| `DEBUG`           | Enable/disable debugging mode       | `True` or `False`   |
+-------------------+--------------------------------------+---------------------+

5. Available Options
--------------------

- Key configurable options in the configuration file and their default values:

+----------------+-------------------------------+------------+---------------------+
| Option         | Description                   | Default    | Allowed Values      |
+================+===============================+============+=====================+
| `DEBUG`        | Enable/disable debugging mode | `False`    | `True` or `False`   |
+----------------+-------------------------------+------------+---------------------+
| `LOG_LEVEL`    | Logging level                | `INFO`     | `DEBUG`, `ERROR`    |
+----------------+-------------------------------+------------+---------------------+
| `MAX_RETRIES`  | Number of retries allowed    | `3`        | Integers >= 1       |
+----------------+-------------------------------+------------+---------------------+

**How to Customize**

1. Edit values directly in the configuration file.
2. Override settings via environment variables.

6. Use Cases
------------

1. **Development Environment**  
   - Use `DEBUG=True` and `LOG_LEVEL=DEBUG`.
2. **Production Environment**  
   - Use `DEBUG=False` and `LOG_LEVEL=ERROR`.
3. **Enable Specific Features**  
   - Example: To enable caching, set `ENABLE_CACHE=True`.

7. Troubleshooting
------------------

1. **Configuration File Not Loading**  
   - Ensure the correct file path is specified.
2. **Environment Variables Not Applied**  
   - Check if the `.env` file is loaded properly:

.. code-block:: bash

   source .env

3. **Check Debug Logs**  
   - Set `LOG_LEVEL=DEBUG` and review the log file.

8. Security Considerations
--------------------------

1. Manage sensitive information (e.g., database passwords) using environment variables, not configuration files.
2. Add configuration files to `.gitignore` to avoid committing them to version control systems.
3. Disable debugging mode (`DEBUG=True`) in production environments.

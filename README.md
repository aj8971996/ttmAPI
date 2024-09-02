# ttmAPI - Table Top Manager API

## Overview

This repository contains the backend implementation of the `ttmAPI`, an Employee Checkout System developed for a homebrewed table top role playing game system. The API is designed to manage and track users (players), character lists, characters, abilitites, and items.

### Key Features

- **Automatic Table and Data Management** The API will check if the necessary tables exist and create them. (This will eventually also include loading sample data for all tables.)
    - If tables do not exist, they will be created.
    - If tables exist - but are of a different structure, they will be modified.
    - If tables exist, and match current structure, the API will provide a success indicator.

- **More to Come**

### Note
- **Development and Testing:** This API is designed to be cloned and ran locally. There is no live server set up.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- **Python 3.12 or higher**: Required for running the FastAPI application and other Python scripts.
- **pip (Python package installer)**: Needed for installing dependencies.
- **MySQL**: A MySQL instance is required for the API’s database operations.

### MySQL Setup
1. **Install MySQL**

   Visit the MySQL Community Installer page to download and install the necessary tools, including MySQL Workbench and MySQL Community Server.

   [MySQL Downloads](https://dev.mysql.com/downloads/)

   **Recommended Downloads:**
   - **MySQL Workbench**: For database management and queries.
   - **MySQL Community Server**: The MySQL server instance.
   - **MySQL Connector(s)**: For connecting applications to the MySQL server.

2. **Create the ECS API User**

   The API requires a specific MySQL user with the necessary privileges. Follow the steps below to create the user:

   1. **Create the User**
      ```sql
      CREATE USER 'ttm_api_user'@'localhost' IDENTIFIED BY 'password';
      ```
   2. **Grant Privileges**
      ```sql
      GRANT ALL PRIVILEGES ON ttm_api.* TO 'ttm_api_user'@'localhost';
      ```
   3. **Commit the Changes**
      ```sql
      FLUSH PRIVILEGES;
      ```
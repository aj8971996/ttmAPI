# ttmAPI - Table Top Manager API

## Overview

This repository contains the backend implementation of the `ttmAPI`, an API designed to manage and track users (players), character lists, characters, abilities, items, and other related entities for a homebrewed tabletop role-playing game system. The API includes endpoints for both Game Masters (GM) and players, enabling robust character management, inventory control, and other game-related operations.

### Key Features

- **User Registration with Password Hashing:**
   - User registration now requires a password and password confirmation.
   - Passwords are hashed securely using industry-standard practices, ensuring that they are not stored in plaintext.

- **JWT Authentication:**
   - Login functionality includes the creation of JWT tokens, ensuring secure authentication for users.

- **Comprehensive Endpoints for GMs and Players:** 
   - GMs can add characters, abilities, expertise, job skills, species passives, items, and weapons.
   - Both GMs and players can manage character inventories, view and adjust character stats, and more.

### Setup Instructions

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

### Python Environment Setup

   1. **Clone the Repository**
      ```bash
      git clone https://github.com/aj8971996/ttmAPI.git
      cd ttmAPI
      ```
   2. **Create and Activate a Virtual Environment (Optional but recommended)**
      ```bash
      python3 -m venv env
      source env/bin/activate  # On Windows use `env\Scripts\activate`
      ```
   3. **Install Dependencies**
      ```bash
      pip install -r requirements.txt
      ```

### Running the API

   1. **Initialize the Database**
   
      Ensure the necessary tables are created or modified to match the current schema:

      ```bash
      python main.py
      ```

   2. **Start the FastAPI Server**
      ```bash
      uvicorn main:app --reload
      ```

   3. **Access the API**

      Once the server is running, the API can be accessed at `http://localhost:8000`.

### API Documentation

FastAPI automatically generates interactive API documentation, which can be accessed at:

   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Available Endpoints

The API provides a wide range of endpoints for both GMs and players. Here are some key endpoints:

   - GM Endpoints
      
      - `POST /gm/add-character`: Add a new character.
      - `POST /gm/add-ability`: Add a new ability.
      - `GET /gm/view-characters`: View all characters.

   - Player and GM Endpoints

      - `POST /player/add-character`: Add a new player character.
      - `GET /player/view-character`: View all characters for a player.
      - `POST /player/level-up`: Level up a character.

### User Registration and Authentication

- **User Registration**:
   - Users can register as either a GM or a Player.
   - Registration requires a username and password. The password is hashed before being stored in the database.
   
- **Login and JWT Authentication**:
   - Users can log in with their username and password.
   - Upon successful login, a JWT token is issued, which is used for authentication in subsequent API requests.

### Modifying the Database Schema
If the database schema changes, the main.py script includes logic to automatically modify existing tables to align with the updated schema without losing data. This ensures that the API remains flexible and can adapt to future changes.
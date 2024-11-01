# Spy Cat Agency

## Overview

This project is a management application for the Spy Cat Agency (SCA). It simplifies the processes of managing spy cats,
missions, and targets.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL (or any other database)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/jirniyjirniy/spy_cat.git
2. Navigate to the project directory:
    ```bash
   cd spy_cat
3. Create a virtual environment:
    ```bash
   python -m venv venv
4. Activate the virtual environment:
    - On macOS/Linux:
    ```bash
   source venv/bin/activate
    ```
    - On Windows
   ```bash
   venv\Scripts\activate
   ```
5. Install the required packages:
    ```bash
   pip install -r requirements.txt

6. Configure the database in settings.py.

7. Apply migrations:
   ``` bash
   python manage.py migrate
   ```

8. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

9. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Endpoints

### Spy Cats

- **List all spy cats**:  
  `GET /api/spy-cats/`

- **Create a spy cat**:  
  `POST /api/spy-cats/`

- **Get a single spy cat**:  
  `GET /api/spy-cats/{id}/`

- **Update a spy cat**:  
  `PUT /api/spy-cats/{id}/`

- **Delete a spy cat**:  
  `DELETE /api/spy-cats/{id}/`

- **Validate breed**:  
  `POST /api/spy-cats/{id}/validate_breed/`

### Missions

- **List all missions**:  
  `GET /api/missions/`

- **Create a mission**:  
  `POST /api/missions/`

- **Get a single mission**:  
  `GET /api/missions/{id}/`

- **Update a mission**:  
  `PUT /api/missions/{id}/`

- **Delete a mission**:  
  `DELETE /api/missions/{id}/`

- **Complete a target**:  
  `POST /api/missions/{mission_id}/complete_target/{target_id}/`

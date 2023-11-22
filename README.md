# Book store

This project is a test task for likesoft.

## Main Technologies Used

- Python
- Django
- Django-ninja
- MySQL
- Docker

## Deploying the Project

### Requirements
- Docker and Docker Compose installed
- GNU Make (https://www.gnu.org/software/make/)

### Instructions:
1. Clone the repository
   ```bash
   git clone https://github.com/kirillovme/books_store.git
   ```
2. Complete Email settings in .env if needed.
3. Start the containers
   ```bash
   make up-d
   ```
4. Make tests if needed
    ```bash
    make tests
    ```



## Project Branch Structure

- `main` - Current production branch of the project
- `dev` - Main development branch

# test_fastAPi Web Application

Backend Developer Test

## Requirements

- Python 3.7+
- MySQL database

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure the database:
    - Create .env file, example of env file:
    
   `DB_USERNAME=fastapi_user
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_NAME=fastapi_db`

   

## Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs`.

## Endpoints

- **/users/signup**: Sign up a new user.
- **/users/token**: Login and get a token.
- **/posts/**: Add a new post.
- **/posts/**: Get all posts.
- **/posts/{post_id}**: Delete a post.

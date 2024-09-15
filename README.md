# FastAPIintro
A small introduction-to-web-development project. Currently creates a "Hello World" webpage with fastapi.

### Run Project
This project is run using docker compose. To run:
1) [Install docker compose](https://docs.docker.com/compose/install/)
2) Clone this repository:

    ```
    git clone https://github.com/shahaansshah/fastAPIintro
    ```

3) In your CLI, with the repository root directory active, run `docker compose up`
    - If changing/updating the repository, run `docker compose up --build`
4) In your web browser, open `http://localhost:80` (correct this)
5) Once finished, run `docker compose down`

### Test Project Modules
Run `python -m pytest` from the root directory. (Correct this - see Issue #2)
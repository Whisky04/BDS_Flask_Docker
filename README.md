## Requirements

1. Python version 3.11
2. Poetry is installed
3. Docker is installed

## Running the Project

Down here it is described how to run the project on your machine.

1. **Start Docker app.**
   Simply start the Docker on a background.

2. **Change working directory.**
   Navigate to the root directory of the project in your console.

3. **Create a Virtual Environment.**
   Run the following command in the console to create a Virtual Environment:

```bash
python -m venv .venv
```

4. **Activate the Virtual Environment.**
   Run one of the following commands to activate the Virtual Environment:

For Windows:

```bash
.venv\Scripts\activate
```

For Linux/MacOS:

```bash
source .venv/bin/activate
```

5. **Build and Running the project**
   To build and run the project, write the following in the root directory of the project:

```bash
docker-compose up --build
```

## Structure of the Project

Below is an overview of the project's files.

- **app.py**
  A Flask application, that returns "Hello, Docker!" when followed by URL.

- **Dockerfile**
  A script, that creates a Docker image from Python 3.11.9-slim, installs dependencies, copies the app code and runs the project on port 5000.

- **docker-compose.yml**
  A configuration file for Docker Compose that builds and runs the Flask container, mapping port 5000 and setting the environment to development state.

- **requirements.txt**
  A list of Python package dependencies, which are required to run the application.

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

3. **Creation of `.env` files.**  
   In the root of the project, in both frontend and backend folders, create an empty `.env` file. Ask Danylo for data to insert inside.

4. **Build and Running the project.**  
   To build and run the project, write the following in the root directory of the project:

```bash
docker-compose up --build
```

5. **Access the site.**  
   After a successfull compose and run of containers, the site is available by http://localhost:5001.

Question 3: Containers
Dockerise the express.js app and write a dockercompose file that will spin up and expose the app on port 4567. Needed Files are in the express-app folder.

Solution: 
1. Create a Dockerfile
FROM node:18-alpine	//Using the official Node.js image
WORKDIR /usr/src/app	//Setting up the working directory
COPY package*.json ./	//Coping package files and installing dependencies
RUN npm install		//Running in a project folder that contains a package.json file to download dependencies.
EXPOSE 4567		//Expose the port your application runs on

-----------------------------------------------------------

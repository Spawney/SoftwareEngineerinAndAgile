# SoftwareEngineeringAndDevOps
Software Engineering and DevOps Assignment

This is a Python/Django Application, with statically linked files using WhiteNoise.

The application is a database of customer orders for our business (Synectics). 
All parts of the website require you to be signed in.
You can add an order to the database if you have permissions to do so. (CRUD)

The application can be run locally, and included in the repository is a requirements.txt file to load the insall the pre-requisites.
The application is also hosted as an Azure Web App, at the following url : https://softwareengineeringanddevops.azurewebsites.net/

The CI/CD Pipeline is as follows:

- Code is checked in to GitHub repo, which would be a private repository with only contributors given access (unfortunately due to free account restrictions, I have had to keep this public).
- Github is linked to Azure Devops with an Azure Service Connection - this is definied in the pipeline yaml (azure-pipelines-1.yml).
- A trigger in the yml is defined, so that when master is checked into, it triggers the CI pipeline in Azure DevOps.
- A Build stage, and test stage is run.
- After this, there is a requirement for manual authorisation to deploy the application to the Azure Web App.
- A Deploymant stage is then ran

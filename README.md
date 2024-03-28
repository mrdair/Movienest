# TMDB Movies Dataset ELT Pipeline

Welcome to the TMDB Movies dataset ELT (Extract, Load, Transform) pipeline project README. This project automates the process of downloading the TMDB Movies dataset, uploading it to Azure Blob Storage, and then transforming and loading it into Snowflake using Mage, dbt, Google Lookup, and Terraform.

## About the TMDB Movies Dataset

The TMDB Movies dataset contains information about over 900,000 movies and is refreshed daily with all the latest changes, ensuring you have the most current movie data at your fingertips!

## Project Structure


## Setup and Installation

1. **Docker Setup**: Ensure Docker and Docker Compose are installed on your machine.
2. **Azure Blob Storage**: Create a storage account and obtain the necessary credentials (account name, access key).
3. **Snowflake**: Set up a Snowflake account and obtain the connection details (account name, username, password, warehouse name, database name, and schema name).
4. **Google Lookup**: Sign up for Google Cloud services to use Google Lookup for creating diagrams.
5. **Terraform**: Install Terraform for managing infrastructure as code (IaC).

## Usage

### 1. Automated Data Download and Upload

- Run `docker-compose up` to automate the process of downloading the TMDB Movies dataset and uploading it to Azure Blob Storage.
- The Dockerfile and docker-compose.yml automate the setup and execution of this process.

### 2. Data Pipeline with Mage

### 3. Data Transformation with dbt

- Use dbt (`dbt_project.yml` and `transform_data.sql`) to transform the loaded data in Snowflake.
- Customize the transformation SQL scripts as per your data requirements.

### 4. Diagrams with Google Lookup

- Utilize Google Lookup to create architecture and data flow diagrams (`architecture_diagram.png`, `data_flow_diagram.png`).
- Update the diagrams to reflect your specific data pipeline architecture.

## Infrastructure as Code (IaC) with Terraform

- Use Terraform (`main.tf` and `variables.tf`) to provision and manage the infrastructure, including Snowflake, Azure Blob Storage, and other resources.

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests.

## Acknowledgements

- TMDB for providing the Movies dataset.
- Microsoft Azure for Azure Blob Storage.
- Snowflake for the cloud data warehouse.
- Mage for workflow orchestration.
- dbt for data transformation.
- Google Cloud services for Google Lookup.
- Terraform for infrastructure as code.

## Contact

For any questions or feedback, please contact [Mohammadreza Davoodabadi](mailto:mohammadrezadavidabadi@gmail.com).


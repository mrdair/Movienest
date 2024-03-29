# ELT Project: TMDB Movies to Snowflake with Daily Updates

This project automates an Extract, Load, Transform (ELT) pipeline to ingest movie data from the TMDB Movies dataset on Kaggle, store it in Azure Blob Storage, and transform it for use in Snowflake, a cloud data warehouse. The pipeline runs daily to keep your data warehouse up-to-date with the latest movie information.

## Project Overview

This project demonstrates various data engineering techniques:

- **Daily Data Ingestion:** Scheduled download of the TMDB Movies dataset from Kaggle using Docker.
- **Data Storage:** Uploading data to Azure Blob Storage using Docker.
- **Data Orchestration:** Scheduling data pipeline execution with Apache Airflow.
- **Data Warehousing:** Loading and storing data in Snowflake (cloud data warehouse).
- **Data Transformation:** Transforming data using dbt for improved analysis.
- **Infrastructure as Code (IaC):** Provisioning data lake (Azure Blob Storage) and data warehouse (Snowflake) using Terraform.
- **Optional Data Visualization:** Generating simplified two-tier diagrams with Google Looker (for clarity).

## Technologies Used

- Docker: Containerization for data download and upload.
- Docker Compose: Orchestrates Docker containers for streamlined execution.
- Apache Airflow: Schedules and manages data pipeline tasks.
- Snowflake: Cloud-based data warehouse for storing and querying transformed data.
- dbt: Transforms data within Snowflake for improved usability.
- Terraform: IaC tool for provisioning and managing cloud resources (Azure Blob Storage and Snowflake).
- Google Looker (optional): Data visualization tool (for basic diagrams).

## Project Structure

```
.
├── README.md  (This file)
├── data         (Directory for raw data downloaded from Kaggle)
├── docker       (Directory for Dockerfile and docker-compose.yml)
├── airflow      (Directory for Airflow DAGs and configuration)
├── dbt          (Directory for dbt models)
└── terraform    (Directory for Terraform configuration)
    ├── azure      (Configuration for Azure Blob Storage)
    └── snowflake  (Configuration for Snowflake data warehouse)
```

## Getting Started

### Prerequisites

Ensure you have the following installed and set up:

- Docker and Docker Compose
- Azure account with appropriate permissions
- Snowflake account
- dbt Cloud account (free tier available)
- Terraform

### Setup Instructions

1. **Set Up Azure Blob Storage (Terraform):**
   - Edit `terraform/azure/main.tf` with your Azure credentials and desired Blob Storage parameters.
   - Run `terraform init` and `terraform apply` in the `terraform/azure` directory.

2. **Set Up Snowflake Data Warehouse (Terraform):**
   - Edit `terraform/snowflake/main.tf` with your Snowflake credentials and desired data warehouse configuration.
   - Run `terraform init` and `terraform apply` in the `terraform/snowflake` directory.

3. **Configure Airflow (Optional):**
   - Follow Airflow's documentation for configuration if using a local installation.
   - Connect Airflow to your Snowflake data warehouse.

4. **Build and Run Docker Containers:**
   - Build the Docker image: `docker-compose build`
   - Run the containers: `docker-compose up`

5. **Run Airflow DAG (Optional):**
   - Use the Airflow UI or CLI to trigger the DAG manually if not run by Docker containers.

6. **Data Transformation with dbt:**
   - Edit dbt models in the `dbt` directory as per your transformation requirements.
   - Run `dbt run` to execute the dbt models and transform data in Snowflake.

## Optional Data Visualization

Connect Google Looker to your Snowflake data warehouse to create basic two-tier diagrams for visualizing the data flow (data lake -> data warehouse).

## Additional Notes

- Modify the Dockerfile and `docker-compose.yml` for different Kaggle datasets or download locations.
- Adjust Airflow DAGs and dbt models as needed for specific data processing requirements.

## Contact

If you have any questions or require assistance with this project, feel free to reach out: [Mohammadreza Davoodabadi](mailto:mohammadrezadavidabadi@gmail.com).


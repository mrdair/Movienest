# Movinest (Data Engineering Zoomcamp Final Project) - <u>[DataTalksClub](https://datatalks.club/)</u>

This project automates an Extract, Load, Transform (ELT) pipeline to ingest movie data from the TMDB Movies dataset on Kaggle, store it in Azure Blob Storage, and transform it for use in Snowflake, a cloud data warehouse.

## Description

### Objective
The Movinest project aims to automate the Extract, Load, Transform (ELT) pipeline for processing movie data from the TMDB Movies dataset on Kaggle. Leveraging technologies like Apache Airflow, Snowflake, Azure Blob Storage, dbt, and Google Looker, the project streamlines data ingestion, storage, transformation, and visualization processes. The objective is to create a scalable, maintainable, and efficient solution for data engineers and analysts to explore, analyze, and derive insights from a comprehensive collection of movie-related information.

### Dataset 
<u>[The TMDB Movies Dataset 2024](https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates)</u> offers over 900,000 movies with daily updates, providing rich data on titles, genres, ratings, production details, and cast & crew. Explore movie trends, build recommendation systems, or quench your cinematic curiosity with this comprehensive dataset.

### Tools & Technologies 
This project implements a fully automated Extract, Load, Transform (ELT) data pipeline for a Kaggle dataset. It leverages a modern data stack with the following technologies:

- Infrastructure as Code (IaC) - [**Terraform**](https://www.terraform.io)
- Workflow Orchestration - [**Airflow**](https://airflow.apache.org)
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Cloud Data Warehouse - [**Snowflake**](https://www.snowflake.com)
- Cloud Data Lake - [**Azure Blob Storage**](https://azure.microsoft.com/)
- Transformation - [**dbt**](https://www.getdbt.com)
- Visualization - [**Google Looker**](https://lookerstudio.google.com)
- Language - [**Python**](https://www.python.org)

## Key Features

- **Automation:** The entire ELT process is orchestrated by Airflow, running within Docker containers for a consistent and portable environment.
- **Configuration Management:** Environment variables in a `.env` file handle sensitive information.
- **Modular Design:** The pipeline is separated into well-defined stages (download, upload, transformation, visualization) for maintainability.
- **Scalability:** The infrastructure is provisioned using Terraform, allowing for easy scaling as data volume grows.
- **Data Governance:** dbt ensures consistent data transformations and documentation.


## Architecture
![ELT Zoomcamp project ](https://github.com/mrdair/TMDB-Movies-Dataset-ELT-Pipeline/assets/51988179/5f3432d1-f1a0-4468-8e3f-7d2f0ac743bc)

## Getting Started

### Prerequisites

- Docker installed
- Terraform installed
- Airflow configured
- Snowflake account with access
- Azure Blob Storage account with access
- dbt Cloud account (or local dbt setup)
- Google Looker account (optional)

## Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/mrdair/TMDB-Movies-Dataset-ELT-Pipeline.git
    ```

2. **Create `.env` File:**
    - Create a file named `.env` in the project root directory.
    - Add environment variables for sensitive information (e.g., passwords, connection strings) following the format `<KEY>=<VALUE>`. **Example:**

        ```
        KAGGLE_USERNAME=your_kaggle_username
        KAGGLE_API_KEY=your_kaggle_api_key
        AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string
        SNOWFLAKE_ACCOUNT=your_snowflake_account
        SNOWFLAKE_USER=your_snowflake_user
        SNOWFLAKE_PASSWORD=your_snowflake_password
        SNOWFLAKE_WAREHOUSE=your_snowflake_warehouse
        SNOWFLAKE_DATABASE=your_snowflake_database
        SNOWFLAKE_SCHEMA=your_snowflake_schema
        DBT_CLOUD_PROJECT=your_dbt_cloud_project (if using dbt Cloud)
        GOOGLE_LOOKER_CLIENT_ID=your_google_looker_client_id (optional)
        GOOGLE_LOOKER_CLIENT_SECRET=your_google_looker_client_secret (optional)
        ```

3. **Initialize Terraform:**

    ```bash
    cd terraform
    terraform init
    ```

4. **Apply Terraform Configuration:**

    ```bash
    terraform apply
    ```

5. **Configure and Start Airflow:**
    - Follow Airflow's documentation to configure the web UI and scheduler.
    - Start Airflow using Docker:

        ```bash
        cd airflow
        docker-compose up -d
        ```

6. **Set Up dbt:**
    - Set up dbt Cloud or local dbt environment according to your preference.
    - Configure dbt profiles to connect to Snowflake.

7. **Configure Google Looker (Optional):**
    - Create a Looker connection to Snowflake.
    - (Optional) Set up API credentials for Looker integration (if using).

## Contact

If you have any questions or require assistance with this project, feel free to reach out: [Mohammadreza Davoodabadi](mailto:mohammadrezadavidabadi@gmail.com).


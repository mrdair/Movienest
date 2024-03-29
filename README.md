# ELT Project: TMDB Movies to Snowflake with Daily Updates

This project automates an Extract, Load, Transform (ELT) pipeline to ingest movie data from the TMDB Movies dataset on Kaggle, store it in Azure Blob Storage, and transform it for use in Snowflake, a cloud data warehouse. The pipeline runs daily to keep your data warehouse up-to-date with the latest movie information.

## Description

This project implements a fully automated Extract, Load, Transform (ELT) data pipeline for a Kaggle dataset. It leverages a modern data stack with the following technologies:

- **Infrastructure as Code (IaC):** Terraform
- **Workflow Orchestration:** Apache Airflow (Dockerized)
- **Cloud Data Warehouse:** Snowflake
- **Data Lake:** Azure Blob Storage
- **Data Transformation:** dbt
- **Data Visualization:** Google Looker (diagrams)

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


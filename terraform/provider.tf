terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=2.0"
    }
    snowflake = {
      source  = "chanzuckerberg/snowflake"
      version = ">=0.24.0"
    }
  }
}

provider "azurerm" {
  features {}
  # Azure credentials and region configuration
}

provider "snowflake" {
  account  = var.snowflake_account
  username = var.snowflake_username
  password = var.snowflake_password
}

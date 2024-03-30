terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=2.0"
    }
  }
}

provider "azurerm" {
  features {}
  # Azure credentials and region configuration
}

resource "azurerm_storage_container" "example" {
  name                  = "myblobcontainer"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "private"
}

resource "snowflake_database" "example" {
  name        = "mydatabase"
  comment     = "Example Snowflake database"
  managed     = true
}

resource "snowflake_user" "example" {
  name       = "myuser"
  login_name = "myuserlogin"
  password   = "mypassword"
}

# Example output
output "storage_container_url" {
  value = azurerm_storage_container.example.primary_blob_endpoint
}

output "snowflake_database_id" {
  value = snowflake_database.example.id
}

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.97.1"
    }
    
    snowflake = {
      source = "Snowflake-Labs/snowflake"
      version = "0.87.3-pre"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "resourceg50gb"
  location = "East US"
}

resource "azurerm_storage_account" "example" {
  name                     = "storagegg50gb"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    environment = "dev"
  }
}

resource "azurerm_storage_container" "example_container" {
  name                  = "uploads"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "private"
}

data "azurerm_storage_account_sas" "example" {
  connection_string = azurerm_storage_account.example.primary_connection_string
  https_only        = true
  signed_version    = "2017-07-29"

  resource_types {
    service   = true
    container = false
    object    = false
  }

  services {
    blob  = true
    queue = false
    table = false
    file  = false
  }

  start  = "2024-03-21T00:00:00Z"
  expiry = "2025-03-21T00:00:00Z"

  permissions {
    read    = true
    write   = true
    delete  = false
    list    = false
    add     = true
    create  = true
    update  = false
    process = false
    tag     = false
    filter  = false
  }
}

output "storage_account_name" {
  value = azurerm_storage_account.example.name
}

output "storage_account_key" {
  value     = azurerm_storage_account.example.primary_access_key
  sensitive = true
}

output "sas_url_query_string" {
  value = data.azurerm_storage_account_sas.example.sas
  sensitive = true
}
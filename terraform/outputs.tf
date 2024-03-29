output "storage_container_url" {
  description = "URL of the Azure Blob Storage container"
  value       = azurerm_storage_container.example.primary_blob_endpoint
}

output "snowflake_database_id" {
  description = "ID of the Snowflake database"
  value       = snowflake_database.example.id
}

output "snowflake_user_login" {
  description = "Login name of the Snowflake user"
  value       = snowflake_user.example.login_name
}

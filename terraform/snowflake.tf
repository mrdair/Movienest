provider "snowflake" {
  user   = ""
  password   = ""
  account    = ""
}

resource "snowflake_database" "example_db" {
  name = "example_db"
  comment = "Example Snowflake database"
}

resource "snowflake_schema" "example_schema" {
  name = "example_schema"
  database = snowflake_database.example_db.name
}

resource "snowflake_warehouse" "example_warehouse" {
  name = "example_warehouse"
  warehouse_size = "XSMALL"
  comment = "Example Snowflake warehouse"
}


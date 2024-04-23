terraform {
  required_providers {
    google= {
        source  = "hashicorp/google"
        version = "5.13.0"
    }
  }
}


provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}


resource "google_storage_bucket" "airbnb-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
  
}

resource "google_bigquery_dataset" "airbnb-dataset" {
  dataset_id = var.bq_dataset_name
  location = var.location
}
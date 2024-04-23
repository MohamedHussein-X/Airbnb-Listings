variable "credentials" {
  description = "My credentials"
  default = "../keys/my-credits.json"
}

variable "project" {
  description = "project name"
  default = "airbnb-listings-421017" 
}

variable "region" {
  description = "Cloud region"
  default = "us-central1"
}

variable "location" {
  description = "project location"
  default = "US"
}

variable "bq_dataset_name" {
  description = "Big Query dataset name"
  default = "Airbnb_dataset"

}

variable "gcs_bucket_name" {
  description = "GCS bucket name"
  default = "airbnb-listings-421017-bucket"
}

variable "gcs_storage_bucket_class" {
  description = "GCS bucket class"
  default = "standard"
}

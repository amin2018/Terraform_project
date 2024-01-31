provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

data "google_container_cluster" "primary" {
  name     = var.gke_cluster_name
  location = var.gke_cluster_zone

  depends_on = [
    module.gke
  ]
}

data "google_client_config" "default" {}

resource "null_resource" "cluster" {
  triggers = {
    gke_cluster_endpoint = module.gke.gke_cluster_endpoint
  }

  depends_on = [
    module.gke
  ]
}

provider "kubernetes" {
  host                   = "https://${module.gke.gke_cluster_endpoint}"
  token                  = data.google_client_config.default.access_token
  client_certificate     = module.gke.gke_cluster_client_certificate
  client_key             = module.gke.gke_cluster_client_key
  cluster_ca_certificate = module.gke.gke_cluster_ca_certificate
}
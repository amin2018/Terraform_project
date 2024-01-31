// Outputs for the Cloud SQL module
output "instance_ip_address" {
  description = "The IP address of the Cloud SQL instance."
  value       = module.cloud_sql.instance_ip_address
}

output "database_name" {
  description = "The name of the database."
  value       = module.cloud_sql.database_name
}

output "db_user_name" {
  description = "The name of the user."
  value       = module.cloud_sql.db_user_name
}

# // Outputs for the VM module
# output "vm_instance_name" {
#   description = "The name of the virtual machine instance"
#   value       = module.vm.vm_instance_name
# }

# // Outputs for the Persistent Disk module
# output "persistent_disk" {
#   description = "The created persistent disk"
#   value       = module.persistent_disk.disk_self_link
# }

# output "attached_disk" {
#   description = "The attached disk resource"
#   value       = module.persistent_disk.attached_disk
# }

# // Outputs for the GKE module
output "gke_cluster_name" {
  description = "The name of the GKE cluster"
  value       = module.gke.gke_cluster_name
}

output "gke_cluster_endpoint" {
  description = "The endpoint of the GKE cluster"
  value       = module.gke.gke_cluster_endpoint
}

// Outputs for the Kubernetes Deployment module
output "deployment_name" {
  description = "The name of the deployment"
  value       = module.k8s_deployment.deployment_name
}

output "replicas" {
  description = "The number of replicas of the application"
  value       = module.k8s_deployment.replicas
}


// Variables for the Database module
database_name             = "test-database"
db_user_name              = "test-user"
db_user_password          = "1234"
cloud_sql_connection_name = "my-project:us-central1:my-instance"

// Variables for the GCP project
project_id = "gcp-terraform-407918"
region     = "us-central1"
zone       = "us-central1-a"

// Variables for the GKE module
gke_cluster_name = "test-cluster"
gke_cluster_zone = "us-central1-a"
deployment_name  = "app-deployment"
replicas         = 1
image_name       = "us-docker.pkg.dev/gcp-terraform-407918/todoapp/my-image"
image_tag        = "latest"
container_name   = "app"
container_port   = 8080
app_label        = "app"

// Variables for the VM module (currently commented out)
# vm_name = "test-vm"

// Variables for the Persistent Disk module (currently commented out)
# disk_name = "test-disk"
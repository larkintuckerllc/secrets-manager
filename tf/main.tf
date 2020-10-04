locals {
  config_context = "gke_spotify-cram_us-west1-a_starter-kit" # REPLACE
}

provider "kubernetes" {
  config_context = local.config_context
}

module "application" {
  source = "./modules/application"
}

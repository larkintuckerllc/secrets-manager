locals {
  cpu      = "100m"
  image    = "sckmkny/starter-kit-image-python:1.0.0"
  instance = "secrets-manager"
  memory   = "128Mi"
  name     = "secrets-manager"
  version  = "0.1.0"
}

resource "kubernetes_service_account" "this" {
  metadata {
    name = local.instance
    labels = {
      "app.kubernetes.io/instance" = local.instance
      "app.kubernetes.io/name"     = local.name
      "app.kubernetes.io/version"  = local.version
    }
  }
}

resource "kubernetes_deployment" "this" {
  lifecycle {
    ignore_changes = [spec[0].template[0].spec[0].container[0].image]
  }
  metadata {
    name = local.instance
    labels = {
      "app.kubernetes.io/instance" = local.instance
      "app.kubernetes.io/name"     = local.name
      "app.kubernetes.io/version"  = local.version
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        instance = local.instance
      }
    }
    template {
      metadata {
        labels = {
          "app.kubernetes.io/instance" = local.instance
          "app.kubernetes.io/name"     = local.name
          "app.kubernetes.io/version"  = local.version
          instance                     = local.instance
        }
      }
      spec {
        automount_service_account_token  = true
        container {
          image             = local.image
          image_pull_policy = "Always"
          name              = local.name
          liveness_probe {
            http_get {
              path = "/"
              port = "http"
            }
          }
          port {
            container_port = 8080
            name           = "http"
          }
          readiness_probe {
            http_get {
              path = "/"
              port = "http"
            }
          }
          resources {
            limits {
              cpu    = local.cpu
              memory = local.memory
            }
            requests {
              cpu    = local.cpu
              memory = local.memory
            }
          }
          security_context {
            allow_privilege_escalation = false
            # read_only_root_filesystem  = true # ISSUE: tiangolo/meinheld-gunicorn image requires RW filesystem
            run_as_non_root            = true
            run_as_group               = 1000 # ISSUE: https://github.com/hashicorp/terraform-provider-kubernetes/issues/695
            run_as_user                = 1000 # ISSUE: https://github.com/hashicorp/terraform-provider-kubernetes/issues/695
          }
        }
        service_account_name             = kubernetes_service_account.this.metadata[0].name
      }
    }
  }
}

resource "kubernetes_service" "this" {
  metadata {
    name     = local.instance
    labels   = {
      "app.kubernetes.io/instance" = local.instance
      "app.kubernetes.io/name"     = local.name
      "app.kubernetes.io/version"  = local.version
    }
  }
  spec {
    port {
      port        = 80 
      target_port = 8080
    }
    selector = {
      instance = local.instance
    }
    type = "LoadBalancer"
  }
}

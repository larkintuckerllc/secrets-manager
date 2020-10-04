output "service_external_ip" {
  value = module.application.service_external_ip.load_balancer_ingress[0].ip
}

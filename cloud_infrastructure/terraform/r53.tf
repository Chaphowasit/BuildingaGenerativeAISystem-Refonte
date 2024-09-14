### R53 Records ###
resource "aws_route53_record" "www" {
  zone_id = var.r53_zone_id
  name    = var.domain_name
  type    = "A"

  alias {
    name                   = aws_lb.loadbalancer.dns_name
    zone_id                = aws_lb.loadbalancer.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "hello_cert_dns" {
  allow_overwrite = true
  name            = "example.com"  # Replace with the actual record name
  records         = ["value"]      # Replace with the actual record value
  type            = "CNAME"        # Replace with the actual record type
  zone_id         = var.r53_zone_id
  ttl             = 60
}
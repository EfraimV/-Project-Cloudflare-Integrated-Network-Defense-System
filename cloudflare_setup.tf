resource "cloudflare_firewall_rule" "block_tor" {
  zone_id     = var.cloudflare_zone_id
  description = "Block TOR exit nodes"
  filter_id   = cloudflare_filter.tor_nodes.id
  action      = "block"
}

resource "cloudflare_filter" "tor_nodes" {
  zone_id = var.cloudflare_zone_id
  expression = "(cf.threat_score gt 10) or (ip.geoip.is_tor)"
}

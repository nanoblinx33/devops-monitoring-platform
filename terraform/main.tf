terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "monitoring" {
  name = "monitoring-network"
}

resource "docker_volume" "grafana_data" {
  name = "grafana-data"
}

resource "docker_volume" "prometheus_data" {
  name = "prometheus-data"
}

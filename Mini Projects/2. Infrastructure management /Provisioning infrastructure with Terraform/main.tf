terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.38.0"
    }
  }
}


provider "google" {
 

  project = "cs-e4190-alina-khan"
  region  = "us-central1"
  zone    = "us-central1-c"
}


resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}

resource "google_compute_firewall" "allow-internal" {
  name    = "test-firewall"
  network = google_compute_network.vpc_network.name
  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
source_ranges = ["0.0.0.0/0"]
}

variable "vm_name_input" {
  type = string
}

resource "google_compute_instance" "vm_instance" {
  name         = "${var.vm_name_input}"
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.name
    access_config {
    }
  }
}

output "vm_name" {
  value = var.vm_name_input

}

output "public_ip" {
value = google_compute_instance.vm_instance.network_interface.0.access_config[0].nat_ip
}

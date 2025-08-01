variable "subscription_id" {
  description = "Azure subscription ID"
  type        = string
}

variable "public_ssh_key_path" {
  description = "Path to your public SSH key"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}
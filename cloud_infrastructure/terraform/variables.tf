variable "aws-access-key" {
    type = string
    description = "AWS Access Key"
}

variable "aws-secret-key" {
    type = string
    description = "AWS Secret Key"
}
### General Variables ###
variable "domain_name" {
  type        = string
  description = "The domain name for the website."
  default     = "cmcloudlab1035.info"
}

variable "r53_zone_id" {
  type        = string
  description = "The zone ID of the domain you are deploying to, you can get it from R53 DNS Dashboard"
  default     = "Z05010881LJUQQXQQ3LKG"
}

### EC2 Values ###
variable "instance_type" {
  type        = string
  description = "Define the EC2 Instance type for the ecs cluster"
  default     = "t2.micro"
}

### ECS ###
variable "container_image" {
  type        = string
  description = "Define what docker image will be deployed to the ECS task"
  default     = "nginx"
}
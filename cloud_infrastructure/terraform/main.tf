# Example Terraform configuration

provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "app_cluster" {
  name = "app-cluster"
}

resource "aws_ecs_task_definition" "app_task" {
  family                   = "app-task"
  network_mode             = "awsvpc"
  container_definitions    = jsonencode([
    {
      name      = "app-container",
      image     = "your-docker-image",
      essential = true,
      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
        }
      ]
    }
  ])
  requires_compatibilities = ["FARGATE"]
  memory                   = "512"
  cpu                      = "256"
}

resource "aws_ecs_service" "app_service" {
  name            = "app-service"
  cluster         = aws_ecs_cluster.app_cluster.id
  task_definition = aws_ecs_task_definition.app_task.arn
  desired_count   = 1

  network_configuration {
    subnets         = ["subnet-XXXXXX"]
    security_groups = ["sg-XXXXXX"]
    assign_public_ip = true
  }
}

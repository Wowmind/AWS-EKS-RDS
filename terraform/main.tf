# RDS Instance
resource "aws_db_instance" "main" {
  identifier           = "myapp-mysql-rds"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  storage_type         = "gp2"
  db_name              = "todo_db"
  username             = var.db_username
  password             = base64decode(var.db_password)
  parameter_group_name = "default.mysql8.0"

  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name

  multi_az               = false
  publicly_accessible    = false
  skip_final_snapshot    = true

  tags = {
    Name = "MyApp MySQL RDS"
  }
}

# Data source for availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

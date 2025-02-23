from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class ConnectSolutionsAcrossVpcsUsingVpcPeeringStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the DB VPC with CIDR block 10.0.0.0/16
        db_vpc = ec2.Vpc(self, "DbVpc",
            cidr="10.0.0.0/16"
        )
        

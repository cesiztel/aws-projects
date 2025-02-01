from aws_cdk import (
    aws_rds as rds,
    aws_ec2 as ec2,
    core
)

class AuroraServerlessV2Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "AuroraVPC")

        # Create a security group for the Aurora cluster
        security_group = ec2.SecurityGroup(self, "AuroraSecurityGroup",
                                           vpc=vpc,
                                           description="Allow access to Aurora Serverless V2",
                                           allow_all_outbound=True)
        security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(3306), "Allow MySQL access")

        # Create the Aurora Serverless V2 cluster
        cluster = rds.DatabaseCluster(self, "AuroraServerlessV2Cluster",
                                      engine=rds.DatabaseClusterEngine.aurora_mysql(version=rds.AuroraMysqlEngineVersion.VER_3_02_0),
                                      instances=1,
                                      instance_props=rds.InstanceProps(
                                          vpc=vpc,
                                          instance_type=ec2.InstanceType.of(
                                              ec2.InstanceClass.BURSTABLE3,
                                              ec2.InstanceSize.MEDIUM
                                          ),
                                          security_groups=[security_group]
                                      ),
                                      scaling=rds.ServerlessScalingOptions(
                                          auto_pause=core.Duration.minutes(10),  # Auto pause after 10 minutes of inactivity
                                          min_capacity=rds.AuroraCapacityUnit.ACU_2,  # Minimum capacity
                                          max_capacity=rds.AuroraCapacityUnit.ACU_16  # Maximum capacity
                                      )
                                      )

        core.CfnOutput(self, "ClusterEndpoint", value=cluster.cluster_endpoint.hostname)
        core.CfnOutput(self, "ClusterIdentifier", value=cluster.cluster_identifier)
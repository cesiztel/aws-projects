import aws_cdk as core
import aws_cdk.assertions as assertions

from connect_solutions_across_vpcs_using_vpc_peering.connect_solutions_across_vpcs_using_vpc_peering_stack import ConnectSolutionsAcrossVpcsUsingVpcPeeringStack

# example tests. To run these tests, uncomment this file along with the example
# resource in connect_solutions_across_vpcs_using_vpc_peering/connect_solutions_across_vpcs_using_vpc_peering_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ConnectSolutionsAcrossVpcsUsingVpcPeeringStack(app, "connect-solutions-across-vpcs-using-vpc-peering")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

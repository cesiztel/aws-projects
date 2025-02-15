#!/usr/bin/env python3
import os

import aws_cdk as cdk

from ecr_ecs_fargate.ecr_ecs_fargate_stack import EcrEcsFargateStack


app = cdk.App()
EcrEcsFargateStack(app, "EcrEcsFargateStack")

app.synth()

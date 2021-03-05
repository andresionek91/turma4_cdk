#!/usr/bin/env python3

from aws_cdk import core

from turma4_cdk.turma4_cdk_stack import Turma4CdkStack


app = core.App()
Turma4CdkStack(app, "turma4-cdk")

app.synth()

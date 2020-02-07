# -*-coding: utf-8 -*-
#
#
# FC function to run FnF flow
#
#
import json
import logging

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkfnf.request.v20190315.StartExecutionRequest import StartExecutionRequest

logger = logging.getLogger()


def handler(event, context):
    # Init fnf client use sts token
    creds = context.credentials
    sts_creds = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
    fnf_client = AcsClient(credential=sts_creds, region_id=context.region)

    evt = json.loads(event)
    logger.info("Start execution {} ".format(evt))

    payload = evt.get("payload", "{}")
    data = json.loads(payload)
    start_execution(fnf_client, data.get("flow_name", ""), data.get("execution_name", ""), data.get("input", ""), context)


def start_execution(fnf_client, flow_name, execution_name, input, context):
    request = StartExecutionRequest()
    request.set_FlowName(flow_name)
    request.set_ExecutionName(execution_name)
    request.set_Input(input)
    request.set_endpoint("{}-internal.fnf.aliyuncs.com".format(context.region))
    fnf_client.do_action_with_exception(request)

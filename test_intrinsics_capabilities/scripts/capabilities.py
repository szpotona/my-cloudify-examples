from cloudify.manager import get_rest_client
from cloudify_rest_client.filters import Filter
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

client = get_rest_client()
# ctx.logger.info(client.deployments.get(deployment_id='test-intrinsics-capabilities').capabilities)
# ctx.logger.info(client.deployments.get(deployment_id='test-intrinsics-capabilities')['capabilities'])
# filter_dep = {"blueprint_id": "terraform_module"}
# deps = client.deployments.list(**filter_dep)
# for dep in deps:
#     ctx.logger.info(str(dep))
#     ctx.logger.info(str(dep.keys()))

# filters = client.deployments_filters.list()
# for f in filters:
#     ctx.logger.info(str(f))

ctx.logger.info("Node id: " + str(inputs['node_id']))
ctx.logger.info("Node id: " + str(inputs['node_id_prop']))

filter_dep = {"blueprint_id": "update_module"}

filters = [
    {'key': 'blueprint_id', 'values': ['test'], 'operator': 'contains', 'type': 'attribute'}
]
deps = client.deployments.list(sort='updated_at', is_descending=True, filter_rules=filters)
for dep in deps:
    ctx.logger.info(str(dep.latest_execution_status))
    ctx.logger.info(str(dep['latest_execution']))
    ctx.logger.info(str(dep['updated_at']))
    ctx.logger.info(str(dep['created_at']))


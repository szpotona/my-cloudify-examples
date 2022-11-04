from cloudify.workflows import ctx
from cloudify.workflows import parameters as p
from cloudify.manager import get_rest_client
from copy import deepcopy

client = get_rest_client()
ctx.logger.info("Test")
ctx.logger.info(ctx._nodes_and_instances._nodes)
test = ctx._nodes_and_instances._nodes.get(p['disk_node_name'])._node
ctx.logger.info('Deployment id: ' + ctx.deployment.id)
ctx.logger.info('Params: {} {}'.format(p['disk_node_name'], p['disk_sizes']))
properties_list = []
for disk in p['disk_sizes']:
    resource = deepcopy(test.get('properties'))
    resource['resource_config']['deployment']['inputs'] = {"the_value": disk}
    properties_list.append(resource)
scalable_entity_properties = {p['disk_node_name']: properties_list}
ctx.logger.info('Scalable entity properties: {}'.format(str(scalable_entity_properties)))
client.executions.start(workflow_id='scaleuplist',
                        deployment_id=ctx.deployment.id,
                        allow_custom_parameters=True,
                        parameters={"scalable_entity_properties": scalable_entity_properties},
                        queue=True)

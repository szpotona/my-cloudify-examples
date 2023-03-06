from cloudify.workflows import ctx
from cloudify.workflows import parameters as p
from cloudify.manager import get_rest_client

graph = ctx.graph_mode()
ctx.logger.info("Parameters {}".format(str(p)))
for node_instance in ctx.node_instances:
    if node_instance.node.id in p["nodes_to_runon"] and \
            'cloudify.nodes.ansible.Executor' in \
            node_instance.node.type_hierarchy:
        operation = 'custom_actions.upgrade_rr'
        run_data = node_instance.node.properties.get('run_data')
        run_data.update(p["run_data"])
        task = node_instance.execute_operation(operation,
                                               allow_kwargs_override=True,
                                               kwargs={
                                                   "run_data": run_data
                                               })
        ctx.logger.info("Operation: {}".format(operation))
        client = get_rest_client()
        node = client.nodes.get(ctx.deployment.id, node_instance.node.id, evaluate_functions=True)
        ctx.logger.info("Parameters " + str(node.properties['run_data']))
        graph.add_task(task)
graph.execute()

for node_instance in ctx.node_instances:
    if node_instance.node.id in p["nodes_to_runon"] and \
            'cloudify.nodes.terraform.Module' in \
            node_instance.node.type_hierarchy:
        operation = 'terraform.reload'
        task = node_instance.execute_operation(operation,
                                               allow_kwargs_override=True,
                                               kwargs={
                                                   "variables": p["variables"]
                                               })
        ctx.logger.info("Operation: {}".format(operation))
        graph.add_task(task)
graph.execute()

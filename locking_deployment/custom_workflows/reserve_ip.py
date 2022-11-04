from cloudify.workflows import ctx
from cloudify.workflows import parameters as p

ctx.logger.info("Test")
ctx.logger.info('Params: {}'.format(p['vm_id']))
graph = ctx.graph_mode()
for node_instance in ctx.node_instances:
    operation = 'custom.reserve_ip'
    task = node_instance.execute_operation(operation,
                                           allow_kwargs_override=True,
                                           kwargs={"vm_id": p["vm_id"]})
    ctx.logger.info("Operation: {}".format(operation))
    graph.add_task(task)
graph.execute()


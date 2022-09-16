from cloudify.workflows import ctx


graph = ctx.graph_mode()
for node_instance in ctx.node_instances:
    if 'cloudify.nodes.ansible.Executor' in \
            node_instance.node.type_hierarchy:
        operation = 'custom_actions.upgrade_rr'
        task = node_instance.execute_operation(operation)
        ctx.logger.info("Operation: {}".format(operation))
        graph.add_task(task)

for node_instance in ctx.node_instances:
    if 'cloudify.nodes.terraform.Module' in \
            node_instance.node.type_hierarchy:
        operation = 'terraform.update'
        task = node_instance.execute_operation(operation)
        ctx.logger.info("Operation: {}".format(operation))
        graph.add_task(task)
graph.execute()

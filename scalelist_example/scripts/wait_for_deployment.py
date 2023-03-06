from cloudify import ctx
from cloudify.exceptions import RecoverableError
from cloudify.manager import get_rest_client


def wait_for_deployment(dep_id):
    client = get_rest_client()
    executions = client.executions.list(deployment_id=dep_id)
    running_exec_list = [e for e in executions if e.status not in ['failed', 'terminated', 'cancelled']]
    if running_exec_list:
        raise RecoverableError("Waiting for deployment " + dep_id + " to finish all executions")


dep_elements = ctx.deployment.id.split('-')
deployment_index = int(dep_elements[-1])
prev_deployment_index = deployment_index - 1
dep_elements = dep_elements[:-1]
dep_elements.append(str(prev_deployment_index))
prev_deployment_id = "-".join(dep_elements)
ctx.logger.info("Previous dep id: " + prev_deployment_id)
if prev_deployment_index >= 0:
    wait_for_deployment(prev_deployment_id)


with open("/tmp/debug.log", 'a') as f:
    f.write("Debugging Manager 500 error. Deployment id: " + deployment_id + "\n")
    f.write("Component_ids: " + str(components_ids) + "\n")

with open("/tmp/debug.log", 'a') as f:
    f.write("Component: " + component + self.sm.list(models.NodeInstance,filters=node_instance_filter,get_all_results=True,include=['runtime_properties','id'])+ "\n")

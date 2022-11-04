from cloudify.manager import get_rest_client
from cloudify import ctx

client = get_rest_client()
client.secrets.create(ctx.deployment.id, "the value", update_if_exists=False)
ctx.logger.info(client.secrets.get(ctx.deployment.id))
client.secrets.update(ctx.deployment.id, "updated value")
ctx.logger.info(client.secrets.get(ctx.deployment.id))
client.secrets.delete(ctx.deployment.id)

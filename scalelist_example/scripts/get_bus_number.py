from cloudify import ctx

ctx.instance.runtime_properties["number"] = int(ctx.deployment.id.split('-')[-1]) + 1

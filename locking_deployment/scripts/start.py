from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

reserved_ips = ctx.instance.runtime_properties.get('reserved_ips', {})
reserved_ips.update({inputs["vm_id"]: "127.0.0.1"})
ctx.instance.runtime_properties['reserved_ips'] = reserved_ips

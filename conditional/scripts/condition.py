from cloudify import ctx
from cloudify.state import ctx_parameters as inputs


def install_test():
    # here goes super complex condition
    return 1 if inputs["flag"] else 0


ctx.instance.runtime_properties["install_test"] = install_test()

from cloudify import ctx


def agent_installation_download_link(**kwargs):
    with ctx.agent.install_script_download_link(clean=False) as download_link:
        ctx.instance.runtime_properties['download_link'] = str(download_link)


agent_installation_download_link()

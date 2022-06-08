from jupyter_client.localinterfaces import public_ips
from dockerspawner import DockerSpawner
from nativeauthenticator import NativeAuthenticator

image_name = "jpyhub"

c.JupyterHub.authenticator_class = NativeAuthenticator

c.Authenticator.admin_users = {"irie"}

ip = public_ips()[0]
c.JupyterHub.hub_ip = ip
c.JupyterHub.port = 8888

c.JupyterHub.spawner_class = DockerSpawner
c.Spawner.default_url = "/lab"
c.DockerSpawner.default_url = "/lab"
c.DockerSpawner.image = image_name
c.DockerSpawner.remove_containers = True
c.DockerSpawner.hub_ip_connect = public_ips()[0]

notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {"jupyterhub-user-{username}" : notebook_dir}

import simplegcd.Deployer as Deployer

Deployer.PROJECT = "resonant-rock-376300"
Deployer.ZONE = "us-central1-a"

# Deployer.deploy_instance_group(
#     "test-group", "test-instance",
#     "projects/resonant-rock-376300/global/instanceTemplates/instance-template-1", 5)

Deployer.delete_instance_group("test-group")

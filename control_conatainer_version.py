import sys

args = sys.argv
microservice_image = args[1]
microservice_image_tag = args[2]

docker_compose_file = open("/home/project/docker-compose.yaml", "r+")
lines = []
while True:
    line = docker_compose_file.readline()
    if f"registry.gitlab.com/group/project/{microservice_image}" in line:
        changed_line = f"    image: registry.gitlab.com/group/project/{microservice_image}:{microservice_image_tag}\n"
        lines.append(changed_line)
    else:
        lines.append(line)
    if not line:
        break


docker_compose_file = open("/home/project/docker-compose.yaml", "w")
docker_compose_file.writelines(lines)

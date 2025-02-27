Podman OCI / Docker Container Manual
===

Learn how to build the container images using podman/docker. Using podman is highly recommended due to multiuser support via rootless containers. This template support several container environments:

1. macOS (m1-m4, intel)
2. Linux (pc/x86_64, devkit/arm64)

Podman Desktop: https://podman-desktop.io


## Ubuntu Setup:

If you have a server or a linux client you need to install these packages:

```
sudo apt install podman uidmap slirp4netns 
```

### Optional: Setup user storage configuration:

This is **mandatory** if the user home is **stored on an NFS share** or if storage needs to changed to an external drive. You can change the container storage location as follows:


1. Create storage configuration file:
```
mkdir -p ~/.config/containers
touch ~/.config/containers/storage.conf
```

2. Get your primary user id:
```
id -u
```

3. Add storage config to ~/.config/containers/storage.conf:
```
[storage]
driver = "overlay"
runroot = "/run/user/YOUR_PRIMARY_USER_ID"
graphroot = "/mnt/storage/containers/${USER}"
```


## List containers and images

```
podman container ls -a  && podman image ls -a
```


## Remove container and container image

```
podman container rm vcsmistemplate || podman image rm mistemplate || podman image prune
```


## Build aarch64 container image (macOS/m1-m4, arm64)

```
podman build --platform linux/arm64 -f Containerfile.aarch64 -t local/mistemplate:latest .
```


## Build x86_64 container image (pc/x86_64, macOS/intel)

```
podman build --platform linux/amd64 -f Containerfile.x86_64 -t local/mistemplate:latest .
```


## Run container

```
podman container rm vcsmistemplate || podman run -d --interactive --name vcsmistemplate \
  -u root:root \
  -e HOME=/home/vscode \
  -v "$(pwd):/workspaces/vscode" \
  -v "$(pwd)/vscode-container-ext/.vscode-server:/home/vscode/.vscode-server" \
  local/mistemplate:latest \
  /bin/sh -c "while sleep 1000; do :; done"
```

> 🚫 You can't start a container on an NFS share! That includes container volume binds. You need to use a non-NFS location for your project.

> 📦 Start the container, attach to container in VSCode, open directory (/workspaces/vscode). 

## Stop container

```
podman stop vcsmistemplate
```

## Remove container

```
podman container rm vcsmistemplate 
```

## Solving common issues

1. Error on setup VSCode environment.

**Behavior:** Attaching container fails with VSCode copy or mv errors.

**Solution:** Delete vscode-container-ext/.vscode-server/{bin, data, extensions, extensionsCache} and try again.

2. Container modifications do not apply.

**Behavior:** Building a new container has no effect on your dev environment.

**Solution:** Delete the container and container image. Purge cached container artifacts.

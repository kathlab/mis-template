# Container Registry

Learn how to push your container image to a container registry and how to get around on the registry.

**Workflow:**

1. Build container image.
2. Apply tag for container registry.
3. Push to registry.


## Build container image

* [BUILDAH (Container image builder)](./BUILDAH.md)
* [PODMAN.md (Work with containers)](./PODMAN.md)

## Apply tag for container registry

```
podman image tag local/YOURIMAGE:TAG REGISTRY_SERVER:5000/mis_USERNAME_YOURIMAGE:TAG
```

## Push to registry

```
podman push REGISTRY_SERVER:5000/mis_USERNAME_YOURIMAGE:TAG
```


## List registry images

```
curl -X GET https://REGISTRY_SERVER:5000/v2/_catalog
```


## List image tags

```
curl -X GET https://REGISTRY_SERVER:5000/v2/mis_USERNAME_YOURIMAGE/tags/list
```
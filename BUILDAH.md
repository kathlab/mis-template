Buildah OCI Container Manual
===

Learn how to build OCI container images using buildah. This template support several container environments:

1. macOS (m1-m4, intel)
2. Linux (pc/x86_64, devkit/arm64)


## List containers and images

```
buildah containers && buildah images
```


## Remove container and container image

```
buildah rm vcsmistemplate || buildah rmi mistemplate || buildah rmi --purge
```


## Build aarch64 container image (macOS/m1-m4/arm64)

```
buildah build --platform linux/arm64 -f Containerfile.aarch64 -t local/mistemplate:latest .
```


## Build x86_64 container image (pc/x86_64, macOS/intel)

```
buildah build --platform linux/amd64 -f Containerfile.x86_64 -t local/mistemplate:latest .
```

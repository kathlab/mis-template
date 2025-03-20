# macOS + Podman

If you have your project volumes **stored on an external drive**, you may encounter the following error when trying to start a container:

```
Error: statfs ... no such file or directory
```

**Issue:**
The podman machine is unable to access your projects on an external drive.

**Solution:**
The podman machine does not include the path of the project. You can fix this by adding the external drive path as volume when creating the podman machine:

```
podman machine init --memory 8192 --volume /Volumes/ExternalSSD
```

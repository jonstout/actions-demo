# Container image that runs your code
FROM centos:7

# Copies your code file from your action repository to the filesystem path `/` of the container
RUN ls -la /home/runner/work/actions-demo/actions-demo/
COPY /home/runner/work/actions-demo/actions-demo/.github/actions/custom-action/entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]

#!/usr/bin/env python
import click
import os
import sys
import shutil
import docker
import docker.errors
import dockerpty
import subprocess


PROJECT_HOME = os.environ.get('PROJECT_HOME')
SHELL = os.environ.get('SHELL')


@click.group()
def bow():
    if PROJECT_HOME is None:
        die("PROJECT_HOME environment variable must be set for bow to work.")


@bow.command()
@click.option('--image', '-i', help="Specify Docker image for this project.")
@click.option('--bare', '-b', is_flag=True, help="Don't create a container for this project.")
@click.argument('name')
def create(name, image, bare):
    """
    Create a new project.
    """
    if bool(bare) == bool(image):
        raise click.UsageError("Specify either --bare or image using --image.")

    path = get_project_path(name)

    print("Creating %s..." % path)
    try:
        os.mkdir(path)
    except FileExistsError:
        die("%s already exists." % path)

    if not bare:
        print("Creating container with image %s..." % image)
        client = docker.Client()
        try:
            client.create_container(
                image=image,
                name=get_container_name(name),
                hostname=name,
                working_dir='/code/',
                command='tail -f /dev/null',
                tty=True,
                volumes=['/code/'],
                host_config=client.create_host_config(binds={
                    path: {'bind': '/code/', 'mode': 'rw'}
                })
            )
        except docker.errors.APIError as error:
            die(error.explanation.decode())

    enter_project(name)


@bow.command()
@click.argument('name')
def rm(name):
    """
    Remove an existing project and its container.
    """
    path = get_existing_project_path(name)

    click.confirm(
        'Are you sure you want to delete project %s?' % name, abort=True)

    container_name = get_container_name(name)
    client = docker.Client()
    try:
        client.inspect_container(container_name)
    except docker.errors.NotFound:
        pass
    else:
        print("Removing container %s..." % container_name)
        client.remove_container(container_name, v=True, force=True)

    print("Removing %s..." % path)
    shutil.rmtree(path)


@bow.command()
@click.argument('name')
def enter(name):
    """
    Enter project's environment.
    """
    enter_project(name)


@bow.command()
@click.argument('name')
def cd(name):
    """
    Cd to the project's directory.
    """
    path = get_existing_project_path(name)
    run_shell_at(path)


@bow.command()
@click.argument('name')
def stop(name):
    """
    Stop project's container.
    """
    container_name = get_container_name(name)
    client = docker.Client()
    try:
        client.stop(container_name)
    except docker.errors.NotFound:
        pass
    except docker.errors.APIError as error:
        die(error.explanation.decode())


# utilities

def enter_project(name):
    path = get_existing_project_path(name)
    container_name = get_container_name(name)
    client = docker.Client()
    try:
        info = client.inspect_container(container_name)
    except docker.errors.NotFound:
        run_shell_at(path)
        return
    except docker.errors.APIError as error:
        die(error.explanation.decode())

    if not info['State']['Running']:
        client.start(container_name)

    dockerpty.exec_command(client, container_name, '/bin/bash')


def get_existing_project_path(name):
    path = get_project_path(name)
    if not os.path.isdir(path):
        die("No project named %s." % name)
    return path


def get_project_path(name):
    return os.path.join(PROJECT_HOME, name)


def get_container_name(project_name):
    return 'bow-%s' % project_name


def run_shell_at(path):
    subprocess.call(SHELL, cwd=path)


def die(message):
    print(message, file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    bow()

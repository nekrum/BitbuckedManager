import click
from bbmanager.api_client.projects_manage import Projects
from bbmanager.api_client.repositories_manage import Repositories
import asyncio


@click.command()
@click.option("--workspace_name", default=None, help="Name of the worokspace")
def list_projects(workspace_name):
    async def get_projects():
        projects = Projects()
        if workspace_name is not None:
            projects.workspace_name = workspace_name
        response = await projects.get_all_projects()
        await projects.close()
        return response

    projects = asyncio.run(get_projects())
    click.echo(projects)


@click.command()
@click.option("--workspace_name", default=None, help="Name of the worokspace")
@click.option("--project_name", help="Name of the project")
@click.option("--project_key", help="Project key")
@click.option("--project_desc", help="Project description")
def create_project(workspace_name, project_name, project_key, project_desc):
    async def create_project():
        projects = Projects()
        if workspace_name is not None:
            projects.workspace_name = workspace_name
        response = await projects.create_project(
            project_name, project_key, project_desc
        )
        await projects.close()
        return response

    projects = asyncio.run(create_project())
    click.echo(projects)


@click.command()
def list_repositories():
    async def get_repositories():
        repositories = Repositories()
        response = await repositories.get_all_repositories()
        await repositories.close()
        return response

    repositories = asyncio.run(get_repositories())
    click.echo(repositories)


@click.command()
@click.option("--workspace_name", default=None, help="Name of the worokspace")
@click.option("--repository_name", help="Name of the project")
@click.option("--repository_key", help="Project key")
def create_repository(workspace_name, repository_name, repository_key):
    async def create_repository():
        repositories = Repositories()
        response = await repositories.create_repository(
            workspace_name, repository_name, repository_key
        )
        await repositories.close()
        return response

    repositories = asyncio.run(create_repository())
    click.echo(repositories)

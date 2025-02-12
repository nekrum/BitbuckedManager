import click
from bbmanager.api_client.projects_manage import Projects
from bbmanager.api_client.repositories_manage import Repositories
from bbmanager.api_client.branch_manage import Branch
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


@click.command()
@click.option("--repository_name", help="Name of the project")
def list_branch_restrictions(repository_name):
    async def get_branch_restrictions():
        branchs = Branch()
        response = await branchs.get_branch_restrictions(repository_name)
        await branchs.close()
        return response

    repositories = asyncio.run(get_branch_restrictions())
    click.echo(repositories)


@click.command()
@click.option("--repository_name", help="Name of repository")
@click.option("--user", help="User selected")
@click.option("--branch", help="Name of repository")
def remove_pr_restriction(repository_name, user, branch):
    async def remove_pr_restriction():
        branchs = Branch()
        response = await branchs.remove_pr_restriction(repository_name, user, branch)
        await branchs.close()
        return response

    branchs = asyncio.run(remove_pr_restriction())
    click.echo(branchs)

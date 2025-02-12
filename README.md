# BitbuckedManager

The package was created using the PDM package manager. Therefore, any 
modifications to the source code should ideally be made using this manager.

## How to install

To install BitBucketManager from a GitHub repository using pip, run the following command:

```bash
pip install git+https://github.com/nekrum/BitBucketManager.git
```

This command fetches the latest version of the package directly from the GitHub 
repository and installs it in your environment. Make sure you have Git installed
on your system, as pip will use it to clone the repository.

If you are using a virtual environment, it is recommended to activate it before 
installation to keep dependencies isolated. For example, using venv:

```bash
python -m venv env  
source env/bin/activate 
pip install -U pip # Update pip is recommended
pip install git+https://github.com/nekrum/BitBucketManager.git
```

After installation, you can verify it by running:

```bash
list-projects --help
```

This should display the available commands, confirming that the installation was successful.

## Commands

1. list-projects :Lists all projects in a workspace.
        --workspace_name <name>: (Optional) Specifies the workspace to list projects from.

2. create-project: Creates a new project within a workspace.
        --workspace_name <name>: (Optional) Specifies the workspace where the project will be created.
        --project_name <name>: (Required) Name of the new project.
        --project_key <key>: (Required) Unique key identifier for the project.
        --project_desc <description>: (Optional) A description of the project.

3. list-repositories: Lists all repositories available in the system.
(No additional options needed.)

4. create-repository: Creates a new repository within a workspace.
        --workspace_name <name>: (Required) Name of the workspace where the repository will be created.
        --repository_name <name>: (Required) Name of the repository.
        --repository_key <key>: (Required) Unique key identifier for the repository.

5. list-branch-restrictions: Displays all branch restrictions applied to a specific repository.
        --repository_name <name>: (Required) Name of the repository to check restrictions.

6. remove-pr-restriction: Removes a pull request restriction from a branch.
        --repository_name <name>: (Required) Name of the repository.
	--user <name>: (Required) Name of the user whose restriction will be removed.
	--branch <name>: (Required) Branch name from which the restriction will be removed.-V>

## Authentication and Token Refresh Requirements

To authenticate and refresh the Bitbucket API token, BitBucketManager requires 
a .env file with the following environment variables:

```ini
BB_ACCESS_TOKEN=<your_access_token>
BB_BASE_URL=<bitbucket_base_url>
BB_WORKSPACE_NAME=<your_workspace_name>
BB_API_KEY=<your_api_key>
BB_API_SECRET=<your_api_secret>
BB_REFRESH_TOKEN=<your_refresh_token>
```

### How to Set Up the .env File

1. Create a .env file in the root directory of your project.
2. Add the required variables with their respective values.
3. Ensure that your application loads these values using a package like python-dotenv (if necessary).

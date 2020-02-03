#!/usr/bin/env python3
import os

import click
import requests
from requests.auth import HTTPBasicAuth


def tag_release(repo: str, user: str, token: str, tag: str, commit: str):
    response = requests.post(
        f"https://api.github.com/repos/{repo}/git/refs",
        auth=HTTPBasicAuth(user, token),
        headers={"Content-Type": "application/json"},
        json={
            "ref": f"refs/tags/{tag}",
            "sha": f"{commit}",
        },
    )

    if response.status_code == 201:
        click.echo(f"Tag {tag} created")
    elif response.json()["message"] == "Reference already exists":
        click.echo(f"Tag {tag} already exists, skip tagging!")
    else:
        raise Exception(response.json())


def main():
    @click.command()
    @click.option(
        "-r", "--repo", envvar="REPOSITORY", required=True,
        help="GitHub repository (e.g. moneymeets/demo-repo)"
    )
    @click.option(
        "-a", "--api-token", envvar="ACCESS_TOKEN", required=True,
        help="GitHub API token"
    )
    @click.option(
        "-u", "--user", envvar="USER", required=True,
        help="GitHub user (e.g. moneymeets)"
    )
    @click.option(
        "-t", "--tag", envvar="TAG", required=True,
        help="Tag to set (e.g. live/v1)"
    )
    @click.option(
        "-c", "--commit-hash", envvar="COMMIT_HASH", required=True,
        help="Commit Hash (e.g. '59d2e89c36774ee3775050a437c290a6c1afb3db')"
    )
    @click.option("--dry-run/--no-dry-run", default=False,
                  help="If set to true, skip tagging")
    def cli(repo: str, api_token: str, user: str, tag: str, commit_hash: str, dry_run: bool):
        click.echo(f"Tag commit '{commit_hash}' with tag '{tag}'")

        if not dry_run:
            tag_release(repo=repo, user=user, token=api_token, tag=tag, commit=commit_hash)

    cli()


if __name__ == "__main__":
    main()

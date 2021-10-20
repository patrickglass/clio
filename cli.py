#!/usr/bin/env python
import os
import click
import clio

# These would be ideally stored in some secure persistence
accessToken = ''
refreshToken = ''

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")

@cli.command()
@click.option(
    '--domain', prompt=True,
    default=lambda: os.getenv('CLIO_AUTH_DOMAIN'))
@click.option(
    '--client_id', prompt=True,
    default=lambda: os.getenv('CLIO_AUTH_CLIENTID'))
def login(domain):
    """Authenticate against IDP"""
    global accessToken, refreshToken
    click.echo('Login')
    auth = clio.Authorization(domain, client_id)
    auth.DeviceFlow()
    accessToken, refreshToken = auth.Tokens()

@cli.command()
def status():
    click.echo('Status')

if __name__ == '__main__':
    cli()

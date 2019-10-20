import click
import requests

@click.command()
@click.option('--package-name', '-pkg')
def pull_pkg(package_name):
    click.echo("{} beginning package download.".format(package_name))
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google.ico', 'wb').write(r.content)


if __name__ == "__main__":
    pull_pkg()
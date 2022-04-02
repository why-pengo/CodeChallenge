import click


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('files', nargs=-1, type=click.Path())
def main(files):
    """Print all FILES file names."""
    for filename in files:
        f = click.open_file(filename, "r")
        click.echo(f.read())


if __name__ == '__main__':
    main()

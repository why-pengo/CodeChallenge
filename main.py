import click
from challenge.ProcessText import ProcessText


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('files', nargs=-1, type=click.Path())
def main(files):
    """Print all FILES file names."""
    for filename in files:
        f = click.open_file(filename, "r")
        proc_text = ProcessText(f.read())
        click.echo(proc_text.get_words())
        click.echo(proc_text.get_sentences())


if __name__ == '__main__':
    main()

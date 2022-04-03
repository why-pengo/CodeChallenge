import click
from challenge.ProcessText import ProcessText


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('files', nargs=-1, type=click.Path())
def main(files):
    """Process all files passed as args or stdin."""
    for filename in files:
        f = click.open_file(filename, "r")
        proc_text = ProcessText(f.read())
        click.echo(proc_text.get_words())
        click.echo(proc_text.get_sentences())
        click.echo(proc_text.process())
        click.echo(proc_text.get_tagged())
        click.echo(proc_text.get_phrases())


if __name__ == '__main__':
    main()

import click
from .main import consensus_response

@click.command()
@click.option('--query', prompt='Your query', help='The query to process')
@click.option('--max-tokens', default=1000, help='Maximum number of tokens in the response')
@click.option('--temperature', default=0.7, help='Temperature for response generation')
def cli(query, max_tokens, temperature):
    result = consensus_response(query, max_tokens, temperature)
    click.echo(f"Best response: {result['response']}")
    click.echo(f"Voting results: {result['voting_results']}")
    click.echo(f"Participating models: {result['participating_models']}")

if __name__ == '__main__':
    cli()
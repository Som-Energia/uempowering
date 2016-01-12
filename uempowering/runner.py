import os
import json
import click
from uempowering import Empowering

config = {
    'url': os.getenv('EMPOWERING_URL', None),
    'key': os.getenv('EMPOWERING_KEY_FILE', None),
    'cert': os.getenv('EMPOWERING_CERT_FILE', None),
    'company_id': os.getenv('EMPOWERING_COMPANY_ID', None),
    'username': os.getenv('EMPOWERING_USERNAME', None),
    'password': os.getenv('EMPOWERING_PASSWORD', None)
}

@click.group()
@click.pass_context
def uempowering(ctx):
    try:
        ctx.obj['emp'] = Empowering(ctx.obj['config'], debug=False)
    except Exception, e:
        click.echo('Empowering service connection failed')

@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_contract(ctx, ids):
   for id in list(ids):
       click.echo(json.dumps(ctx.obj['emp'].get_contract(id), indent=4))


@uempowering.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def get_measurements(ctx, ids):
   for id in list(ids):
       click.echo(json.dumps(ctx.obj['emp'].get_dh_measurements_by_contract(id), indent=4)) 

@uempowering.command()
@click.pass_context
def get_push_stats(ctx):
    click.echo(json.dumps(ctx.obj['emp'].get_all_results('OT900'), indent=4))


if __name__ == '__main__':
    uempowering(obj={'config': config})
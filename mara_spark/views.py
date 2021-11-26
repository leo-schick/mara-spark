import flask
from mara_page import acl, navigation

blueprint = flask.Blueprint('mara_spark', __name__, url_prefix='/')


acl_resource = acl.AclResource(name='Spark')


def navigation_entry():
    return navigation.NavigationEntry(
        label='Spark', uri_fn=lambda: flask.url_for('mara_spark.spark'),
        icon='bar-chart', description='Spark Master website')



@blueprint.route('/spark')
@acl.require_permission(acl_resource)
def spark():
    from . import config

    return flask.redirect(config.external_spark_url())
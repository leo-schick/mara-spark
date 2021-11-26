
def MARA_CONFIG_MODULES():
    from . import config
    return [config]

def MARA_FLASK_BLUEPRINTS():
    from . import views
    return [views.blueprint]

def MARA_CLICK_COMMANDS():
    return []

def MARA_ACL_RESOURCES():
    from .views import acl_resource
    return {'Spark': acl_resource}

def MARA_NAVIGATION_ENTRIES():
    from . import views
    return {'Spark': views.navigation_entry()}
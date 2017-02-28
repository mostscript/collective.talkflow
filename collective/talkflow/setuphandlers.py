

def uninstall_base(context):
    gs = context.getSite().portal_setup
    if u'collective.talkflow:install-base' in gs._profile_upgrade_versions:
        # make safe for reinstall...
        del(gs._profile_upgrade_versions[u'collective.talkflow:install-base'])


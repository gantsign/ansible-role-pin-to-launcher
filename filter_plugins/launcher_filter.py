import re

from jinja2.filters import contextfilter


@contextfilter
def to_dockbarx_items(context, pin_to_launcher_favorites):
    '''
    returns the DockbarX launcher items
    '''

    pin_to_launcher_favorites = list(pin_to_launcher_favorites)

    omit = context.resolve('omit')

    launcher_items = []

    for favourite in pin_to_launcher_favorites:
        application = favourite.get('application')
        if application not in ('', None, omit):
            when_desktop = favourite.get('when_desktop')
            if when_desktop in ('dockbarx', None):
                application_id = favourite.get('application_id')
                if application_id is None:
                    application_id = re.sub(
                        '(.*)\\.desktop$', '\\1', application)
                launcher_items.append(
                    application_id +
                    ';/usr/share/applications/' +
                    application)

    return launcher_items


@contextfilter
def to_gnome_items(context, pin_to_launcher_favorites):
    '''
    returns the Gnome launcher items
    '''

    pin_to_launcher_favorites = list(pin_to_launcher_favorites)

    omit = context.resolve('omit')

    launcher_items = []

    for favourite in pin_to_launcher_favorites:
        application = favourite.get('application')
        if application not in ('', None, omit):
            when_desktop = favourite.get('when_desktop')
            if when_desktop in ('gnome', None):
                launcher_items.append("'" + application + "'")

    return launcher_items


@contextfilter
def to_unity_items(context, pin_to_launcher_favorites):
    '''
    returns the Unity launcher items
    '''

    pin_to_launcher_favorites = list(pin_to_launcher_favorites)

    omit = context.resolve('omit')

    launcher_items = []

    for favourite in pin_to_launcher_favorites:
        application = favourite.get('application')
        if application not in ('', None, omit):
            when_desktop = favourite.get('when_desktop')
            if when_desktop in ('unity', None):
                launcher_items.append("'application://" + application + "'")

        unity = favourite.get('unity')
        if unity not in ('', None, omit):
            launcher_items.append("'unity://" + unity + "'")

    return launcher_items


class FilterModule(object):
    ''' Launcher filter '''

    def filters(self):
        return {
            'to_dockbarx_items': to_dockbarx_items,
            'to_gnome_items': to_gnome_items,
            'to_unity_items': to_unity_items
        }

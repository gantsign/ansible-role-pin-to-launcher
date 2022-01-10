from jinja2.filters import contextfilter


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


class FilterModule(object):
    ''' Launcher filter '''

    def filters(self):
        return {
            'to_gnome_items': to_gnome_items
        }

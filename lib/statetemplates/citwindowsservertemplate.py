from windowsservertemplate import WindowsServerTemplate


class CITWindowsServerTemplate(WindowsServerTemplate):
    """
    Set:
    exists
    name
    url
    username
    password
    priority
    productionstate
    groups
    systems
    deviceclass
    location
    Not Set:

    get_current_state_object implemented:
    True

    get_state_object implemented:
    True
    """

    def __init__(self, record=None, username=None, password=None, url=None,  priority=30, productionstate=None,
                 additional_groups='', additional_systems='', location_override=None):
        super(CITWindowsServerTemplate, self).__init__(record, username, password, url, priority,
                                                     productionstate, additional_groups, additional_systems,
                                                     location_override)

        self.config['deviceclass'] = '/Server/Microsoft/Windows/CIT'
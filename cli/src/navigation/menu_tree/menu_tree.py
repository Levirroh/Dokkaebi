#region online Dokka

ONLINE_ACTIONS_PING = {
    "id": "online_actions_ping",
    "label": "Ping",
    "type": "action",
    "title": "Ping",
    "description": "Pings a device by entering their IP.",
    "requires": ["online", "Dokka VPN"],
    "action": "backend_request",
    "payload": {
        "method": "GET",
        "url": "/agent/ping/:ip"
    }
}

ONLINE_ACTIONS_TREE = {
    "id": "online_actions",
    "label": "Actions",
    "type": "folder",
    "title": "Actions",
    "description": "Execute commands on online devices.",
    "requires": ["online"],
    "children": [ONLINE_ACTIONS_PING],
}


ONLINE_DASHBOARD_NODE = {
    "id": "online_dashboard",
    "label": "Dashboard",
    "type": "screen",
    "title": "Dashboard",
    "description": "Shows online devices and their stats.",
    "requires": ["online"],
    "screen": "dashboard",
}


ONLINE_DOKKA_TREE = {
    "id": "online_dokka",
    "label": "Connect to Dokkaebi",
    "type": "folder",
    "title": "ONLINE Dokkaebi",
    "description": (
        "Enters online mode if configured.\n"
        "Provides a menu with all online capabilities."
    ),
    "requires": ["online"],
    "children": [
        ONLINE_ACTIONS_TREE,
        ONLINE_DASHBOARD_NODE,
    ],
}

#endregion

#region local tests

LOCAL_TESTS_LINK = {
    "id": "local_tests_link",
    "label": "Link Dokka",
    "type": "screen",
    "title": "Connect a new local device",
    "description": "Tries connection with a device in the same network.",
    "requires": ["local_network"],
    "screen": "link_dokka",
}


LOCAL_TESTS_ENDPOINTS = {
    "id": "local_tests_endpoints",
    "label": "Try endpoints",
    "type": "screen",
    "title": "Endpoint Testing",
    "description": "Opens a menu for endpoint testing.",
    "requires": [],
    "screen": "local_endpoints",
}

LOCAL_TESTS_TREE = {
    "id": "local_tests",
    "label": "Local Tests",
    "type": "folder",
    "title": "Local Testing",
    "description": "Provides a menu with all offline actions.",
    "requires": [],
    "children": [
        LOCAL_TESTS_LINK,
        LOCAL_TESTS_ENDPOINTS,
    ],
}

#endregion

#region settings

SETTINGS_NODE = {
    "id": "settings",
    "label": "Settings",
    "type": "screen",
    "title": "Settings",
    "description": "Provides a menu with all configs for Dokkaebi.",
    "screen": "settings",
}

#endregion


#region exit

EXIT_NODE = {
    "id": "exit",
    "label": "Exit",
    "type": "action",
    "title": "Exit",
    "description": "Press ENTER to exit.",
    "warnings": ["This action will leave the application."],
    "action": "exit",
}

RETURN_NODE = {
    "id": "return",
    "label": "Return",
    "type": "action",
    "title": "Return",
    "description": "Go back to previous menu.",
    "action": "return",
}

#endregion


MAIN_TREE = {
    "id": "main",
    "label": "Main Menu",
    "title": "Main Menu",
    "type": "folder",
    "children": [
        ONLINE_DOKKA_TREE,
        LOCAL_TESTS_TREE,
        SETTINGS_NODE,
        EXIT_NODE,
    ],
}
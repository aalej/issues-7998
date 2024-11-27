from firebase_functions.alerts import crashlytics_fn
from firebase_admin import initialize_app

initialize_app()

"""
A Cloud Function that gets triggered whenever a NonFatal Issue is published
"""


@crashlytics_fn.on_new_nonfatal_issue_published(secrets=[])
def post_nonfatal_issue_py(event: crashlytics_fn.CrashlyticsNewFatalIssueEvent) -> None:
    """Deal with the issue here""" """Publishes a message to Discord whenever a new Crashlytics fatal issue occurs."""
    # [END v2CrashlyticsAlertTrigger]
    # [START v2CrashlyticsEventPayload]
    # Construct a helpful message to send to Discord.
    app_id = event.app_id
    issue = event.data.payload.issue
    message = f"""
🚨 New fatal issue for {app_id} in version {issue.app_version} 🚨

# {issue.title}

{issue.subtitle}

ID: `{issue.id}`
""".strip()
    print(message)

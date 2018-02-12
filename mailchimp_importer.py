import requests
import hashlib
import settings


def import_guidebook_metrics_into_mailchimp(event):
    """
    Takes the 'Attendee Created' metrics event and updates a Mailchimp List with the email of the created Attendee
    """
    # this Integration can handle the "Attendee Created" event
    if event['event'] != 'Builder-AttendeeCreatedEvent':
        return

    # Guidebook users created via SAML/SSO login have fake emails (<uuid>@example.com). If you are
    # using an SSO-enabled App, we do not advise that you use the MailChimp Integration - your users
    # do not give Guidebook an email address when signing up
    if '@example.com' in event['properties']['attendee_email']:
        return

    attendee_email = event['properties']['attendee_email'].lower()

    # in order to create or update a list member on mailchimp via PUT, we must calculate
    # the MD5 hash of the lowercased email and use that in the URL
    attendee_email_md5_hash = hashlib.md5(attendee_email).hexdigest()

    mailchimp_list_create_member_url = '{}/3.0/lists/{}/members/{}/'.format(settings.MAILCHIMP_API_ENDPOINT, settings.MAILCHIMP_LIST_ID, attendee_email_md5_hash)
    list_member_put_data = {
        'email_address': attendee_email,  # subscribe this email to the list
        'status': 'subscribed',  # if the member already exists, change them to subscribed
        'status_if_new': 'subscribed',  # if the member is new, they should be added as subscribed
    }
    response = requests.put(mailchimp_list_create_member_url, auth=requests.auth.HTTPBasicAuth('anystring', settings.MAILCHIMP_API_KEY), json=list_member_put_data)
    if response.status_code != 200:
        raise Exception("Failed Mailchimp List Member Creation - {} {}".format(response.status_code, response.content))

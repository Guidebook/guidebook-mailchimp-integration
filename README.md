# About

This code provides an example of how to export Guidebook metrics data into MailChimp.

It takes metrics data from the [Guidebook Webhooks API](https://developer.guidebook.com/#webhooks) and imports it into MailChimp via the [MailChimp REST API](https://developer.mailchimp.com/documentation/mailchimp/guides/get-started-with-mailchimp-api-3/).


# Sample Usage

Before testing out the code.  Please `pip install -r requirements.txt` to get the package dependencies.  We highly recommend you do this in an [virtualenv](https://virtualenv.pypa.io/en/stable/).

Update `settings.py` with your MailChimp API information. Then the following command will perform the import with the demo data in `sample_event.json`.

`python execute_integration`

# Customizing this Integration

This code is provided to Guidebook clients to customize for their own integrations.  Clients are welcome to take this integration code as a starting point and adapt it to their own needs.
import json

import mailchimp_importer

if __name__ == "__main__":
    """
    Reads the demo data from 'sample_event.json' and imports it into MailChimp
    """
    f = open('sample_event.json')
    gb_metrics_event = json.loads(f.read())
    f.close()

    print 'Importing Metrics Data into MailChimp'

    mailchimp_importer.import_guidebook_metrics_into_mailchimp(gb_metrics_event)

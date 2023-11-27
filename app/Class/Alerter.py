from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

class Alerter:
    def __init__(self, token, email):
        self.token = token
        self.email = email

    def send_alert(self,obj, content):
                
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = self.token

        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        sender = {"name":"Alerte","email":"alerte@mail.com"}
        to = [{"email":self.email}]
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=content, sender=sender, subject=obj)
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            print("E-mail envoyé avec succès!")    
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

# test = Alerter('','lenaig.plantec@gmail.com')
# test.send_alert('Alertetest','test')
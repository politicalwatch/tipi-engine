from sparkpost import SparkPost

from alerts.settings import API_SPARKPOST


class emailScrap(object):

    @staticmethod
    def send_mail( message, title):
        sp = SparkPost(API_SPARKPOST)
        doc = message
        response = sp.transmissions.send(
            recipients=["javier.perez@ciecode.es","pablo.martin@iciecode.es"],  # email is a user's email
            html=doc,
            from_email="scrap@tipiciudadano.es",
            subject=title,
            attachments=[
                            {
                                "name": "failed.log",
                                "type": "text/plain",
                                "filename": "failed.log"
                            }
                        ],
        )

        print "reporting..."

# -*- coding: utf-8 -*-

import time
import random
from database.congreso import Congress
from twitteraccount_by_group import TWITTERACCOUNT_BY_GROUP



class TBMessage:

    def __init__(self):
        random.seed(time.time())
        self.dbmanager = Congress()
    
    def random_topic(self):
        random.seed(time.time())
        return random.choice(list(self.dbmanager.getDictByGroup('tipi')))

    def get_message(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Every friday
class StaticMessage(TBMessage):

    MESSAGES = [
            u'¿Has leído lo que la prensa ha contado sobre @Tipi_Ciudadano desde su estreno? Hazlo aquí: https://tipiciudadano.es/medios',
            u'¿Sabes cómo se sitúa la clasificación de los temas más tratados en el @Congreso_es? Descúbrelo aquí: https://tipiciudadano.es/estadisticas',
            u'Busca con nuestro escáner las últimas novedades en el @Congreso_es de los asuntos que más te interesan aquí: https://tipiciudadano.es/escaner',
            u'¿Te has dado de alta ya en nuestro sistema de alertas para conocer cómo se tratan tus temas de interés en el @Congreso_es? https://tipiciudadano.es/signup'
            ]
    
    def get_message(self):
        return random.choice(self.MESSAGES)


class LatestInitiativesByTopicMessage(TBMessage):

    def get_message(self):
        try:
            topic = self.random_topic()
            return u"Descubre aquí cuáles son las últimas iniciativas de %s presentadas en el @Congreso_es, y sus diputados y grupos más activos https://tipiciudadano.es/temas/%s" % (topic['name'].upper(), topic['slug'])
        except:
            pass


class LatestInitiativesByBestDeputyMessage(TBMessage):

    def get_message(self):
        try:
            random_topic_name = self.random_topic()['name']
            best_deputy_name = self.dbmanager.getBestDeputyByTopic(random_topic_name)
            best_deputy = self.dbmanager.getDeputyByName(best_deputy_name)
            if best_deputy['twitter'] == "":
                best_deputy_name = best_deputy_name.split(',')
                best_deputy_name.reverse()
                best_deputy['twitter'] = " ".join(best_deputy_name)
            else:
                best_deputy['twitter'] = "@" + best_deputy['twitter'].split('/')[3]
            return u"Éstas son las últimas iniciativas de %s que ha presentado %s, uno de los diputados más activos en esta temática: https://tipiciudadano.es/dips/%s" % (random_topic_name.upper(), best_deputy['twitter'], best_deputy['_id'])
        except:
            pass


class LatestInitiativesByGroupMessage(TBMessage):

    def get_message(self):
        try:
            random_topic_name = self.random_topic()['name']
            best_group_name = self.dbmanager.getBestGroupByTopic(random_topic_name)
            best_group = self.dbmanager.getGroupByName(best_group_name)
            best_group['twitter'] = TWITTERACCOUNT_BY_GROUP[best_group_name]
            return u"Éstas son las últimas iniciativas de %s que ha presentado %s, uno de los grupos parlamentarios más activos en esta temática: https://tipiciudadano.es/grupos/%s" % (random_topic_name.upper(), best_group['twitter'], best_group['_id'])
        except:
            pass


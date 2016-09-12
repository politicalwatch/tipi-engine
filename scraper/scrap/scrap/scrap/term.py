# -*- coding: utf-8 -*-
import re
import pdb

dicc = {
    #Z para los que no tengan
     # u'Autorización de Convenios Internacionales': ["C","DS"],
     # u'Comisión permanente':["D"],
     # u'Comisión de Investigación':["D"],
     # u'Otras Comisiones no permanentes':["D"],
     # u'Comparecencia de autoridades y funcionarios en Comisión':["DS"],
     # u'Comparecencia del Gobierno ante el Pleno':["DS"],
     # u'Comparecencia del Gobierno en Comisión':["DS"],
     # u'Otras comparecencias en Comisión':["DS"],
     # u'Comunicación del Gobierno':["D"],
     # u'Declaración Institucional':["D"],
     # u'Información sobre Convenios Internacionales':["C"],
     # u'Iniciativa legislativa popular':["B"],
     # u'Interpelación urgente':["D","DS"],
     # u'Interpelación ordinaria':["D","DS"],
     # u'Moción consecuencia de interpelación ordinaria':["D"],
     # u'Moción consecuencia de interpelación urgente':["D"],
     # u'Operaciones de las Fuerzas Armadas en el exterior':["D"],
     # u'Otras solicitudes de informe':["Z"],
     # u'Otros asuntos relativos a Convenios Internacionales':["Z"],
     # u'Planes y programas':["D"],
      u'Pregunta al Gobierno con respuesta escrita':["D"],
     # u'Pregunta oral al Gobierno en Comisión':["D","DS"],
     # u'Pregunta oral en Pleno':["D","DS"],
     # u'Proposición de ley de Grupos Parlamentarios del Congreso':["B"],
     # u'Proposición de ley de Diputados':["B","DS"],
     # u'Proposición de ley de Comunidades y Ciudades Autónomas':["B"],
     # u'Proposición de ley del Senado':["B"],
     # u'Proposición de reforma del Reglamento del Congreso':["B"],
     # u'Proposición no de Ley ante el Pleno': ["D"],
     # u'Proposición no de Ley en Comisión':["D"],
     # u'Proyecto de ley': ["A"],
     # u'Real Decreto-Ley':["D","DS"],
     # u'Real Decreto legislativo que aprueba texto refundido': ["D"],
     # u'Solicitud de creación de Comisión de Investigación':["D"],
     # u'Solicitud de creación de Comisión permanente':["D","DS"],
     # u'Solicitud de creación de otras Comisiones no permanentes':["D","DS"],
     # u'Solicitud de creación de Subcomisiones y Ponencias':["D"],
     # u'Solicitud de informe a la Administración del Estado':["D"],
     # u'Subcomisiones y Ponencias':["D"],

}





class Terms(object):
    @staticmethod
    def getDict():
        return dicc
    @staticmethod
    def getTypetext(key):
        return Terms.getDict()[key]

    @staticmethod
    def getKeys():
        return Terms.getDict().keys()

    @staticmethod
    def getValues():
        return Terms.getDict().values()

    @staticmethod
    def getType(string):
        return [type for type in Terms.getKeys() if re.search(type, string)][0]



    @staticmethod
    def filterBytype(string):
        res = False
        # elimino los art y demas
        newchain =  re.sub('( [\(|\{].*?.$)|(.$)', '' , string.strip())
        for type in Terms.getKeys():
            if re.match(newchain,type):

                res= True
                break
        return res

    @staticmethod
    def isTextvalid(type,serie):
        res = False
        values = Terms.getTypetext(type)
        if values:
            for a in values:
                if re.search(a,serie):
                    res = True
                    break
            return res
        else:
            return None


    @staticmethod
    def whatisthis(s):
        if isinstance(s, str):
            print "ordinary string"
        elif isinstance(s, unicode):
            print "unicode string"
        else:
            print "not a string"

class DocumentInfos:

    title = u"Fonctionnement d'un processeur"
    first_name = 'Joël'
    last_name = 'Truttmann'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Avril'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "Version finale"
    repository_url = "https://github.com/josquell/travail-perso-template"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()
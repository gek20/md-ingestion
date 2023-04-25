from .recherchedatagouv import BaseRDG
from ..service_types import SchemaType, ServiceType


class UnistraDatacite(BaseRDG):
    IDENTIFIER = 'unistra'
    TITLE = 'Université de Strasbourg'
    URL = 'https://entrepot.recherche.data.gouv.fr/oai'
    SCHEMA = SchemaType.DataCite
    SERVICE_TYPE = ServiceType.OAI
    OAI_METADATA_PREFIX = 'oai_datacite'
    OAI_SET = 'unistra'               # Set from entrepot unistra
    PRODUCTIVE = True
    DATE = ''
    DESCRIPTION = """"""
    LOGO = ''
    LINK = ''
    REPOSITORY_ID = ''
    REPOSITORY_NAME = ''
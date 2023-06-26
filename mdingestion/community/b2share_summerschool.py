from .base import Repository
from ..service_types import SchemaType, ServiceType


class BaseSummerschool(Repository):
    IDENTIFIER = 'summerschool'
    TITLE = 'Summer School Kajaani'
    PRODUCTIVE = False
    DATE = '2023-06-27'
    CRON_DAILY = False
    LINK = 'https://eudat.eu/summer-schools/eudat-summer-school-2023'
    LOGO = ""
    DESCRIPTION = """EUDAT Summer School 2023 will be hosted between 26 and 30 of June 2023 in Kajaani, Finland.This edition, organised in collaboration with the DICE project, aims to strengthen the skills required to excel in data management, getting the participants geared up to manage and process data throughout the full, research-data lifecycle (data discovery; data processing; data analysis; data preservation and publishing). Experienced trainers will guide the students combining traditional theoretical lessons with hands-on sessions."""
    # REPOSITORY_ID = ''
    # REPOSITORY_NAME = ''

    def update(self, doc):
        if not doc.publisher:
            doc.publisher = 'EUDAT B2SHARE'
        if not doc.publication_year:
            doc.publication_year = self.find('header.datestamp')


class SummerschoolEudat(BaseSummerschool):  
    IDENTIFIER = 'summerschool_eudat'
    URL = 'https://vm0897.kaj.pouta.csc.fi/api/oai2d'
    SCHEMA = SchemaType.Eudatcore
    SERVICE_TYPE = ServiceType.OAI
    OAI_METADATA_PREFIX = 'eudatcore'
    OAI_SET = 'e9b9792e-79fb-4b07-b6b4-b9c2bd06d095'

    def update(self, doc):
        if not doc.resource_type:
            doc.resource_type = 'Dataset'
        if not doc.discipline:
            doc.discipline = 'Social/Natural Sciences'
        if not doc.contact:
            doc.contact = 'somecrazyemail@coolrepo.eu, www.anyhelpdesk.eu'


class KajaaniSummerschool(BaseSummerschool):  
    IDENTIFIER = 'summerschool_2023'
    URL = 'https://vm0897.kaj.pouta.csc.fi/api/oai2d'
    SCHEMA = SchemaType.Eudatcore
    SERVICE_TYPE = ServiceType.OAI
    OAI_METADATA_PREFIX = 'eudatcore'
    OAI_SET = '06acf21c-7e65-4360-8306-62b781121096'

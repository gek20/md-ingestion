from .base import Repository
from ..service_types import SchemaType, ServiceType


class NiluIso19139(Repository):
    IDENTIFIER = 'nilu'
    URL = 'https://ebas-oai-pmh.nilu.no/oai/provider'
    SCHEMA = SchemaType.ISO19139
    SERVICE_TYPE = ServiceType.OAI
    OAI_METADATA_PREFIX = 'iso19139'
    # OAI_SET = None
    PRODUCTIVE = False
    CRON_DAILY = False
    DATE = '2023-02-01'
    LOGO = "http://b2find.dkrz.de/images/communities/nilu_logo.png"
    DESCRIPTION = """NILU, the Norwegian Institute for Air Research is an independent, nonprofit institution established in 1969. Through its research NILU increases the understanding of processes and effects of climate change, of the composition of the atmosphere, of air quality and of hazardous substances. Based on its research, NILU markets integrated services and products within the analytical, monitoring and consulting sectors. NILU is concerned with increasing public awareness about climate change and environmental pollution. NILUs near 200 researchers, technicians and other experts are primarily commissioned by the Research Council of Norway and by Norwegian and international industry and government agencies. The institute takes an active part in the EUs research programs.
    """
    LINK = 'https://www.nilu.no/'
    REPOSITORY_ID = ''
    REPOSITORY_NAME = ''

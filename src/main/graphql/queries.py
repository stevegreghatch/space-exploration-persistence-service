import strawberry
from typing import List, Optional
from src.main.mongo import DbClient
from src.main.graphql.schemas import AstronautType, DurationType, MissionType


def astronauts(self) -> List[AstronautType]:
    """Get astronauts"""
    result = []
    for entity in DbClient.db.astronauts.find():
        result.append(AstronautType(
            first_name=entity.get('first_name'),
            last_name=entity.get('last_name'),
            programs=entity.get('programs'),
            missions=entity.get('missions'),
            image_url=entity.get('image_url')
        ))
    return result


def astronauts_by_program(self, program: str) -> List[AstronautType]:
    """Get astronauts by program"""
    result = []
    for entity in DbClient.db.astronauts.find({"programs": {"$in": [program]}}):
        result.append(AstronautType(
            first_name=entity.get('first_name'),
            last_name=entity.get('last_name'),
            programs=entity.get('programs'),
            missions=entity.get('missions'),
            image_url=entity.get('image_url')
        ))
    return result


def project_mercury(self) -> List[MissionType]:
    """Get all missions from the db"""
    result = []
    for entity in DbClient.db.project_mercury.find():
        duration_list = DurationType(
            days=entity.get('duration').get('days'),
            hours=entity.get('duration').get('hours'),
            minutes=entity.get('duration').get('minutes'),
            seconds=entity.get('duration').get('seconds')
        )
        result.append(MissionType(
            mission=entity.get('mission'),
            spacecraft_number=entity.get('spacecraft_number'),
            call_sign=entity.get('call_sign'),
            astronaut=entity.get('astronaut'),
            launch_time=entity.get('launch_time'),
            launch_site=entity.get('launch_site'),
            duration=duration_list,
            orbits=entity.get('orbits'),
            apogee_mi=entity.get('apogee_mi'),
            perigee_mi=entity.get('perigee_mi'),
            velocity_max_mph=entity.get('velocity_max_mph'),
            miss_mi=entity.get('miss_mi')
        ))
    return result


def project_mercury_by_call_sign(self, call_sign: str) -> Optional[MissionType]:
    """Get a mission from the db by call sign"""
    for entity in DbClient.db.project_mercury.find({"call_sign": call_sign}):
        duration_list = DurationType(
            days=entity.get('duration').get('days'),
            hours=entity.get('duration').get('hours'),
            minutes=entity.get('duration').get('minutes'),
            seconds=entity.get('duration').get('seconds')
        )
        return MissionType(
            mission=entity.get('mission'),
            spacecraft_number=entity.get('spacecraft_number'),
            call_sign=entity.get('call_sign'),
            astronaut=entity.get('astronaut'),
            launch_time=entity.get('launch_time'),
            launch_site=entity.get('launch_site'),
            duration=duration_list,
            orbits=entity.get('orbits'),
            apogee_mi=entity.get('apogee_mi'),
            perigee_mi=entity.get('perigee_mi'),
            velocity_max_mph=entity.get('velocity_max_mph'),
            miss_mi=entity.get('miss_mi')
        )
    return None


@strawberry.type
class Query:
    """Query type for the GraphQL schema"""
    astronauts: List[AstronautType] = strawberry.field(resolver=astronauts)
    astronauts_by_program: List[AstronautType] = strawberry.field(resolver=astronauts_by_program)
    project_mercury: List[MissionType] = strawberry.field(resolver=project_mercury)
    project_mercury_by_call_sign: Optional[MissionType] = strawberry.field(resolver=
                                                                           project_mercury_by_call_sign)

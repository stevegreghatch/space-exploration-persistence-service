import strawberry
from typing import List
from src.main.mongo import DbClient
from src.main.graphql.schemas import MissionType, DurationType


def missions(self) -> List[MissionType]:
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


@strawberry.type
class Query:
    """Query type for the GraphQL schema"""
    missions: List[MissionType] = strawberry.field(resolver=missions)

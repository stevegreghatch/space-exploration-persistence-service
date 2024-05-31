import strawberry
from typing import List
from src.main.mongo import DbClient
from src.main.graphql.schemas import ProgramType, MissionType, DurationType, AstronautType


def programs(self) -> List[ProgramType]:
    """Get all programs"""
    result = []
    for entity in DbClient.db.programs.find():
        result.append(ProgramType(
            program=entity.get('program'),
            image_url=entity.get('image_url')
        ))
    return result


def missions(self) -> List[MissionType]:
    """Get all missions"""
    result = []
    for entity in DbClient.db.missions.find():
        duration_list = DurationType(
            days=entity.get('duration').get('days'),
            hours=entity.get('duration').get('hours'),
            minutes=entity.get('duration').get('minutes'),
            seconds=entity.get('duration').get('seconds')
        )
        result.append(MissionType(
            mission=entity.get('mission'),
            astronauts=entity.get('astronauts'),
            program=entity.get('program'),
            call_sign=entity.get('call_sign'),
            image_url=entity.get('image_url'),
            spacecraft_number=entity.get('spacecraft_number'),
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


def missions_by_program(self, program: str) -> List[MissionType]:
    """Get all missions from program"""
    result_set = DbClient.db.missions.find({'program': program})
    result = []
    for entity in result_set:
        duration_list = DurationType(
            days=entity.get('duration').get('days'),
            hours=entity.get('duration').get('hours'),
            minutes=entity.get('duration').get('minutes'),
            seconds=entity.get('duration').get('seconds')
        )
        result.append(MissionType(
            mission=entity.get('mission'),
            astronauts=entity.get('astronauts'),
            program=entity.get('program'),
            call_sign=entity.get('call_sign'),
            image_url=entity.get('image_url'),
            spacecraft_number=entity.get('spacecraft_number'),
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


def astronauts_by_mission(self, mission: str) -> List[AstronautType]:
    """Get all missions from program"""
    result_set = DbClient.db.astronauts.find({'missions': mission})
    result = []
    for entity in result_set:
        result.append(AstronautType(
            astronaut_first_name=entity.get('astronaut_first_name'),
            astronaut_last_name=entity.get('astronaut_last_name'),
            image_url=entity.get('image_url'),
            missions=entity.get('missions')
        ))
    return result


@strawberry.type
class Query:
    """Query type for the GraphQL schema"""
    programs: List[ProgramType] = strawberry.field(resolver=programs)
    missions: List[MissionType] = strawberry.field(resolver=missions)
    missions_by_program: List[MissionType] = strawberry.field(resolver=missions_by_program)
    astronauts_by_mission: List[AstronautType] = strawberry.field(resolver=astronauts_by_mission)

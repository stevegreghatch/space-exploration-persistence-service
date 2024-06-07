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
            missions=entity.get('missions'),
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
            launch_date_utc=entity.get('launch_date_utc'),
            launch_mass_lbs=entity.get('launch_mass_lbs'),
            launch_site=entity.get('launch_site'),
            launch_site_coord=entity.get('launch_site_coord'),
            launch_vehicle=entity.get('launch_vehicle'),
            orbits=entity.get('orbits'),
            apogee_nmi=entity.get('apogee_nmi'),
            perigee_nmi=entity.get('perigee_nmi'),
            landing_date_utc=entity.get('landing_date_utc'),
            landing_site=entity.get('landing_site'),
            landing_site_coord=entity.get('landing_site_coord'),
            recovery_ship=entity.get('recovery_ship'),
            duration=duration_list
        ))
    return result


def astronauts(self) -> List[AstronautType]:
    """Get all astronauts from program"""
    result = []
    for entity in DbClient.db.astronauts.find():
        result.append(AstronautType(
            astronaut_first_name=entity.get('astronaut_first_name'),
            astronaut_last_name=entity.get('astronaut_last_name'),
            image_url=entity.get('image_url'),
            missions=entity.get('missions')
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
            launch_date_utc=entity.get('launch_date_utc'),
            launch_mass_lbs=entity.get('launch_mass_lbs'),
            launch_site=entity.get('launch_site'),
            launch_site_coord=entity.get('launch_site_coord'),
            launch_vehicle=entity.get('launch_vehicle'),
            orbits=entity.get('orbits'),
            apogee_nmi=entity.get('apogee_nmi'),
            perigee_nmi=entity.get('perigee_nmi'),
            landing_date_utc=entity.get('landing_date_utc'),
            landing_site=entity.get('landing_site'),
            landing_site_coord=entity.get('landing_site_coord'),
            recovery_ship=entity.get('recovery_ship'),
            duration=duration_list
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
    astronauts: List[AstronautType] = strawberry.field(resolver=astronauts)
    missions_by_program: List[MissionType] = strawberry.field(resolver=missions_by_program)
    astronauts_by_mission: List[AstronautType] = strawberry.field(resolver=astronauts_by_mission)

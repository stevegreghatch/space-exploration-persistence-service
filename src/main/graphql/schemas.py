import strawberry
from typing import List
from space_exploration_common_lib.model.Astronaut import Astronaut
from space_exploration_common_lib.model.mission.ProjectMercury import Mission
from space_exploration_common_lib.model.Duration import Duration


@strawberry.experimental.pydantic.type(model=Astronaut)
class AstronautType:
    """ Astronaut type"""
    first_name: str
    last_name: str
    programs: List[str]
    missions: List[str]
    image_url: str


@strawberry.experimental.pydantic.type(model=Duration, all_fields=True)
class DurationType:
    """ Duration type"""
    pass


@strawberry.experimental.pydantic.type(model=Mission)
class MissionType:
    """ Mission type"""
    mission: strawberry.auto
    spacecraft_number: strawberry.auto
    call_sign: strawberry.auto
    astronaut: strawberry.auto
    launch_time: strawberry.auto
    launch_site: strawberry.auto
    duration: DurationType
    orbits: strawberry.auto
    apogee_mi: strawberry.auto
    perigee_mi: strawberry.auto
    velocity_max_mph: strawberry.auto
    miss_mi: strawberry.auto

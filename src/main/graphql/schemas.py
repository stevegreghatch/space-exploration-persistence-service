import strawberry

from space_exploration_common_lib.model.Program import Program
from space_exploration_common_lib.model.Duration import Duration
from space_exploration_common_lib.model.Mission import Mission
from space_exploration_common_lib.model.Astronaut import Astronaut


@strawberry.experimental.pydantic.type(model=Program, all_fields=True)
class ProgramType:
    pass


@strawberry.experimental.pydantic.type(model=Duration, all_fields=True)
class DurationType:
    pass


@strawberry.experimental.pydantic.type(model=Mission, all_fields=True)
class MissionType:
    pass


@strawberry.experimental.pydantic.type(model=Astronaut, all_fields=True)
class AstronautType:
    pass

import itertools
from enum import Enum
from typing import Any

# .pyd available through PYTHONPATH, see DDS manual
import ProSivicDDS as psvdds

from pedestrian_generator.prosivic_tcp import ProsivicTCP
from pedestrian_generator.pedestrian import Pedestrian


class Direction(Enum):
    Left = 1
    Right = 2


FEMALE_PEDESTRIAN_NAME = "female/pedestrian"
FEMALE_PEDESTRIAN_OBSERVER = "female_observer"
SCRIPT_FILENAME = "scenario1.script"
DISTANCE_TO_ROAD = 8
PEDESTRIAN_SPEED = 2

distances = range(20, 160, 10)
directions = [Direction.Left, Direction.Right]
angles = range(30, 170, 20)


def main() -> None:
    tcp = ProsivicTCP()
    tcp.connect()
    tcp.load(SCRIPT_FILENAME)
    tcp.synchro()

    female_pedestrian = Pedestrian(FEMALE_PEDESTRIAN_NAME, tcp)
    female_pedestrian_observer = psvdds.manObserverHandler(FEMALE_PEDESTRIAN_OBSERVER)

    for direction, distance, angle in itertools.product(directions, distances, angles):
        run_scenario_configuration(
            tcp,
            female_pedestrian,
            female_pedestrian_observer,
            direction,
            distance,
            angle,
        )


def run_scenario_configuration(
    tcp: ProsivicTCP,
    pedestrian: Pedestrian,
    pedestrian_observer: Any,
    direction: Direction,
    distance: int,
    angle: int,
) -> None:
    if direction is Direction.Left:
        start_position_y = DISTANCE_TO_ROAD
        direction_angle = -angle
    else:
        start_position_y = -DISTANCE_TO_ROAD
        direction_angle = angle

    end_position_y = -start_position_y

    # TODO: Does  z=0 work in all situations?
    pedestrian.set_position(distance, start_position_y, 0)
    pedestrian.set_angle(direction_angle)

    tcp.play()

    pedestrian.set_speed(PEDESTRIAN_SPEED)
    data = pedestrian_observer.receive()

    if direction is Direction.Left:
        while data.Human_coordinate_Y > end_position_y:
            data = pedestrian_observer.receive()
    if direction is Direction.Right:
        while data.Human_coordinate_Y < end_position_y:
            data = pedestrian_observer.receive()

    tcp.pause()

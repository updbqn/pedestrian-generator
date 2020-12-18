from .prosivic_tcp import ProsivicTCP


class Pedestrian:
    def __init__(self, name: str, prosivic_tcp: ProsivicTCP) -> None:
        self.name = name
        self.prosivic_tcp = prosivic_tcp

    def set_position(self, x: float, y: float, z: float) -> None:
        self.prosivic_tcp.cmd(f"{self.name}.SetInitPosition {x} {y} {z}")
        self.prosivic_tcp.cmd(f"{self.name}.SetPosition {x} {y} {z}")

    def set_angle(self, z: float) -> None:
        self.prosivic_tcp.cmd(f"{self.name}.SetInitAngle 0 0 {z}")
        self.prosivic_tcp.cmd(f"{self.name}.SetAngle 0 0 {z}")

    def set_speed(self, speed: float) -> None:
        self.prosivic_tcp.cmd(f"{self.name}.SetSpeed {speed}")

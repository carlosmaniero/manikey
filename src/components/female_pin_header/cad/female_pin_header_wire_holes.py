from __future__ import annotations
import manifold3d
from dataclasses import dataclass
from components.female_pin_header.model import FemalePinHeaderModel


@dataclass
class FemalePinHeaderWireHolesBaseCAD:
    model: FemalePinHeaderModel

    def create_housing(self, pins: int) -> manifold3d.Manifold:
        extra_width = 3.0
        extra_structure = manifold3d.Manifold.cube(
            [
                self.model.outer_length(pins),
                extra_width,
                self.model.outer_height,
            ],
            center=True,
        ).translate([0.0, self.model.outer_width / 2 + extra_width / 2, 0.0])

        holes = manifold3d.Manifold()
        for col in range(pins):
            x = (col - (pins - 1) / 2) * self.model.parameters.pitch
            hole = manifold3d.Manifold.cube(
                [1.2, 1.2, self.model.outer_height + 0.2],
                center=True,
            ).translate([x, self.model.outer_width / 2 + extra_width / 2, 0.0])
            holes += hole

        return extra_structure - holes

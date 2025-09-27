from datetime import date
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("NotVaccinatedError")

        today = date.today()
        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < today:
            raise OutdatedVaccineError("OutdatedVaccineError")

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError("NotWearingMaskError")

        return f"Welcome to {self.name}"

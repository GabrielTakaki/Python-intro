import main


PEOPLE_AT_CONCERT_PER_SQUARE_METER = 2  # average number of people per square meter
FIELD_LENGTH = 240  # meters
FIELD_WIDTH = 45  # meters
PEOPLE_AT_CONCERT = main.rectangle(FIELD_LENGTH, FIELD_WIDTH) // PEOPLE_AT_CONCERT_PER_SQUARE_METER


print("Estão presentes no show aproximadamente", PEOPLE_AT_CONCERT, "pessoas")

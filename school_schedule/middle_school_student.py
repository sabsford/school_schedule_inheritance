from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes,
        gets_transportation=False, clubs=None):

        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
        self.clubs = clubs if clubs is not None else []

    def join_club(self, club_name):
        self.clubs.append(club_name)

    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_transportation_message()
        club_message = self.display_clubs()

        return "\n".join((student_summary, transportation_message, club_message))

    def display_transportation_message(self):
        has_message = "has" if self.gets_transportation else "doesn't have"
        return f"{self.name} {has_message} transportation privileges"

    def display_clubs(self):
        club_str = ", ".join(self.clubs)

        if club_str:
            return f"{self.name} is a member of: {club_str}"
    
        return f"{self.name} hasn't joined a club yet."
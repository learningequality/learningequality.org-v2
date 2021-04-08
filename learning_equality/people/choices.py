from django.db.models import TextChoices

# Field choice Enumeration types
# see https://docs.djangoproject.com/en/3.0/releases/3.0/#enumerations-for-model-field-choices
class PersonType(TextChoices):
    """
    categories for team members
    """

    CURRICULUM = "curriculum", "Curriculum & Pedagogy"
    IMPLEMENTATIONs = "implementations", "Program Implementations"
    PARTNERSHIPS = "partnerships", "Partnerships"
    ENGINEERING = "engineering", "Engineering"
    UX = "UX", "UX Design & Research"
    COMMUNICATIONS = "communications", "Communications"
    OPERATIONS = "operations", "Team Operations"
    BOARD = "board", "Board of directors"
    ADVISORS = "advisory", "Advisory Board"

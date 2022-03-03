""""Examples of importing in Python."""


from lessons import helpers

#  Alias a module / imported names as another name
#  One or the other (above) can be made
from lessons import helpers as hp

#  import names defined globally
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")  # Added later on
    print(powerful(2, 4))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()
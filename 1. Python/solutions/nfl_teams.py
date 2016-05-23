"""Prompt the user for either an NFL conference and division or the name of an NFL team.
Based on the response, return either a list of teams in that division or the name of the team's division.

>>> get_teams_by_conference_and_division({'foo':{'bar':['baz']}}, 'foo', 'bar')
['baz']

>>> get_conference_and_division_by_team_name({'foo':{'bar':['baz']}}, 'baz')
('foo', 'bar')
"""


def get_teams_by_conference_and_division(teams, conference, division):
    """Return a list of teams names for the given conference and division or None if there is no match

    >>> NFL = {
    ...     'AFC': {
    ...         'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
    ...         'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers'],
    ...         'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
    ...         'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
    ...     },'NFC': {
    ...         'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
    ...         'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
    ...         'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
    ...         'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']
    ...     }
    ... }

    >>> get_teams_by_conference_and_division(NFL, 'NFC', 'West')
    ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']

    >>> get_teams_by_conference_and_division(NFL, 'AFC', 'East')
    ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets']
    """

    try:
        return teams[conference][division]
    except KeyError:
        return None


def get_conference_and_division_by_team_name(teams, team_name):
    """Return a tuple of the conference and division for the given team name or None if there is no match

    >>> NFL = {
    ...     'AFC': {
    ...         'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
    ...         'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers'],
    ...         'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
    ...         'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
    ...     },'NFC': {
    ...         'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
    ...         'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
    ...         'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
    ...         'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']
    ...     }
    ... }

    >>> get_conference_and_division_by_team_name(NFL, 'New England Patriots')
    ('AFC', 'East')

    >>> get_conference_and_division_by_team_name(NFL, 'Seattle Seahawks')
    ('NFC', 'West')
    """

    for conference in teams.keys():
        for division in teams[conference].keys():
            try:
                if teams[conference][division].index(team_name) > -1:
                    return conference, division
            except ValueError:
                continue

    return None, None


def main(teams):
    """Prompt for user input, get a result from the data, print a nicely formatted answer"""

    user_input = input('Enter the name of either a conference (AFC or NFC) or team: ')

    if user_input in teams.keys():
        conference = user_input
        division = input('Enter the name of a division (North, South, East, West): ')
        teams = get_teams_by_conference_and_division(teams, conference, division)

        if teams is None:
            main(teams)
        else:
            print('The following are the teams in the {conference} {division}:\n• {teams}'.format(
                conference=conference,
                division=division,
                teams='\n• '.join(teams)
            ))

    else:  # assume they input a team name
        team_name = user_input
        conference, division = get_conference_and_division_by_team_name(teams, team_name)

        if conference is None:
            main(teams)
        else:
            print('The {team_name} play in the {conference} {division}.'.format(
                team_name=team_name,
                conference=conference,
                division=division
            ))


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    NFL_TEAMS = {
        'AFC': {
            'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
            'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers'],
            'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
            'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
        },
        'NFC': {
            'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
            'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
            'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
            'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']
        }
    }

    main(NFL_TEAMS)

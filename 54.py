def get_super_series_winner(scores: list):
    canada = 0
    ussr = 0
    for game in scores:
        if game[0] > game[1]:
            canada += 1
        elif game[0] == game[1]:
            canada += 1
            ussr += 1
        else:
            ussr += 1
    if canada > ussr:
        return 'canada'
    elif canada == ussr:
        return None
    else:
        return 'ussr'

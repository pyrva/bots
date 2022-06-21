import raffle_bot


def test_admin_says_pick_me():
    raffle_bot.submissions = set()

    msg = raffle_bot.response(
        msg='pick me',
        author='admin',
        admin=True,
    )

    assert raffle_bot.submissions == set()
    assert msg is None


def test_user_says_pick_me():
    raffle_bot.submissions = set()

    msg = raffle_bot.response(
        msg='pick me',
        author='user',
        admin=False,
    )

    assert raffle_bot.submissions == {'user'}
    assert 'good luck' in msg.lower()


def test_user_already_submitted():
    raffle_bot.submissions = {'user'}

    msg = raffle_bot.response(
        msg='pick me',
        author='user',
        admin=False,
    )

    assert raffle_bot.submissions == {'user'}
    assert 'no worries' in msg.lower()


def test_user_picks_winner():
    raffle_bot.submissions = {'user'}

    msg = raffle_bot.response(
        msg='pick winner',
        author='user',
        admin=False,
    )

    assert raffle_bot.submissions == {'user'}
    assert msg is None


def test_admin_picks_winner_with_entries():
    raffle_bot.submissions = {'user'}

    msg = raffle_bot.response(
        msg='pick winner',
        author='admin',
        admin=True,
    )

    assert raffle_bot.submissions == set()
    assert 'congratulations' in msg.lower()
    assert 'user' in msg


def test_admin_picks_winner_without_entries():
    raffle_bot.submissions = set()

    msg = raffle_bot.response(
        msg='pick winner',
        author='admin',
        admin=True,
    )

    assert raffle_bot.submissions == set()
    assert 'nobody' in msg.lower()

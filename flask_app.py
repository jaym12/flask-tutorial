__author__ = 'jdevdesign'


def age_app():
    user_age = input("What is your age?")
    age_seconds = int(user_age) * 365 * 24 * 60 * 60
    print('Your age in seconds is {}'.format(age_seconds))


age_app()

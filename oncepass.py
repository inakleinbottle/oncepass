
import getpass
import os



def once_pass(env_name="MY_SECRET_PASSWORD"):
    """
    Get the password once from the user in a given session
    and store it in an environment variable that can be 
    accessed again from within the session.
    
    In practice, you'd call this function once at the beginning
    of your session and, if the environment variable is not
    already set you will be prompted for the password. Otherwise,
    the password will be read from the environment.
    """

    if env_name in os.environ:
        return os.environ[env_name]

    password = getpass.getpass()
    os.environ[env_name] = password
    return password


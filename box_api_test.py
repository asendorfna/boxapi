# https://github.com/box/box-python-sdk
# https://developer.box.com/sdks-and-tools/
# https://developer.box.com/reference/

from boxsdk import OAuth2, Client
from boxsdk.object.collaboration import CollaborationRole
from datetime import datetime

# 5 days in seconds
UPDATE_TIME = 60*60*24*5
CREDS_FILE = '../box_creds/box_oauth_creds.txt'
#CREDS_FILE = '../box_creds/box_jwt_creds.txt'

'''
Returns:
- True -> successfully updated
- False -> failed to update
- None -> did not need to update
'''
def update_collaboration_expiration(client, id):
    collaboration = client.collaboration(collab_id=id).get()

    expiration_date = datetime.fromisoformat(collaboration['expires_at'])
    tz = expiration_date.tzinfo
    current_date = datetime.now(tz)

    # Do some math - is this within 5 days?
    timedelta = expiration_date - current_date
    if timedelta.total_seconds() < UPDATE_TIME:

        # If so, update the collaboration date
        new_exp_date = ''
        collaboration_update = {'role': CollaborationRole.EDITOR, 'expires_at': new_exp_date}
        updated_collaboration = collaboration.update_info(data=collaboration_update)

        # Ensure update - return True/False
        return updated_collaboration['expires_at'] == new_exp_date
    else:
        return None

def read_creds(filename):

    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    
    return OAuth2(client_id=lines[0], client_secret=lines[1], 
                  access_token=lines[2])

def run_main():
    
    # Available here: https://nih.app.box.com/developers/console/app/2094055/configuration
    # Looks like you need to update the access token every hour
    # but there is a programatic way to do this via JWTAuth - see github repo above
        
    auth = read_creds(CREDS_FILE)
    client = Client(auth)

    current_user = client.user().get()
    print(current_user)

    # Update this with all user ids that we want to automate
    user_id_list = [current_user]

    successful_updates = 0
    unsuccessful_updates = 0 
    no_updates_needed = 0

    for user_id in user_id_list:
        user_collaborations = get_collaborations()
        for collab_id in user_collaborations:
            res = update_collaboration_expiration(client, collab_id)
            if res is not None:
                if res:
                    print ("Successfully updated CollabID {0} for user {1}".format(collab_id, user_id))
                    successful_updates+=1
                else:
                    print ("Failed to update CollabID {0} for user {1}".format(collab_id, user_id))
                    unsuccessful_updates+=1
            else:
                print ("No update needed for CollabID {0} for user {1}".format(collab_id, user_id))
                no_updates_needed+=1

    print("Update Summary")
    print("No updates need: {}".format(no_updates_needed))
    print("Successful updates: {}".format(successful_updates))
    print("Failed updates: {}".format(unsuccessful_updates))

if __name__ == "__main__":
    run_main()
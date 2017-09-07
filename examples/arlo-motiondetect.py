from Arlo.Arlo import Arlo

USERNAME = 'user@example.com'
PASSWORD = 'supersecretpassword'

try:

    # Instantiating the Arlo object automatically calls Login(), which returns an oAuth token that gets cached.
    # Subsequent successful calls to login will update the oAuth token.
    arlo = Arlo(USERNAME, PASSWORD)
    # At this point you're logged into Arlo.

    # Get the list of devices.
    devices = arlo.GetDevices()
    
    # Get the list of devices and filter on device type to only get the basestation.
    # This will return an array which includes all of the basestation's associated metadata.
    basestations = [ device for device in devices if device['deviceType'] == 'basestation' ]
    
    basestation_id = basestations[0]['deviceId']
    xcloud_id = basestations[0]['xCloudId']

    # Define a callback function that will get called once for each motion event.
    def callback(arlo, basestation_id, xcloud_id, event):
        # Here you will have access to self, basestation_id, xcloud_id, and the event schema.
        print("motion event detected!")
	#print(event)
	#print(arlo)

    # Subscribe to motion events. This method blocks until the event stream is closed. (You can close the event stream in the callback if you no longer want to listen for events.)
    arlo.SubscribeToMotionEvents(basestation_id, xcloud_id, callback)
except Exception as e:
    print(e)
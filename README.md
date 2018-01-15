# Using Raspberry Pi + IR Motion Sensor + Google Cloud Messaging + Android

This is a quick experiment where an IR motion sensor connected to my Pi3, sends data to an Android app, via the GCM.

## Here's the Flow
1. Raspberry Pi (I used Pi 3) with a Raspbian installation
2. A DIY IR motion sensor (you can find some on Amazon)
3. An Android device
4. A GCM API Key
5. An android app registered with your GCM API
6. App server with the Registration ID from step 5
7. Raspberry Pi uses the Registration ID to push notifications to client through the GCM server
8. GCM Server pushes the notifications to the Android app 

_Pictures of the Pi and sensor wiring coming soon...but feel free to beat me to it ;)_

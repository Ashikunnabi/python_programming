"""   SEND SMS FROM COMPUTER USING AirMore APP    """
"""
    - Need to install AirMore application in your smartphone
    - install pyairmore in your computer. Command: pip install pyairmore
"""

from ipaddress import IPv4Address  # for your IP address
from pyairmore.request import AirmoreSession  # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages

def send_sms(mobile_number, message, ip_address, port=2333):
    # let's create an IP address object
    ip = IPv4Address(ip_address)
    # now create a session
    # here default port is 2333. If your one is diffrent then replace 2333 with your one
    session = AirmoreSession(ip, port)

    if session.is_server_running:  
        # True if Airmore is running
        if session.request_authorization(): 
            # True if Airmore session is authorized       
            service = MessagingService(session)
            service.send_message(mobile_number, message)
            print('SMS send successfully to', mobile_number)
        else: 
            print('You are unauthorized')
    else:
        print('Your session is not active')


web_ip_address = "192.168.0.0"    # collect the ip from AirMore app
mobile_number = '011XXXXXXXX'
message = 'Type your message...'

send_sms(mobile_number, message, web_ip_address)
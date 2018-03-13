# Senior-Design-Code
# This code is for testing the motion sensor

import RPi.GPIO as GPIO
import time
from bottle import route, request, run, get

GPIO.setmode(GPIO.BCM)

pin_to_circuit = 18

@route('/led')
def led():
        return #WHAT IS THIS
<htm@route('/led')
def led():
    return '''
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.css">
<script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
<script src="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.js"></script>
<script>
$(document).ready(function() {
  $("#ckLED").change(function() {
    var isChecked = $("#ckLED").is(":checked") ? 1:0; 
    $.ajax({
            url: '/action',
            type: 'POST',
            data: { strID:'ckLED', strState:isChecked }
    });
  });
});
</script>
</head>
<body>
<div data-role="page">
  <div data-role="main" class="ui-content">
    <form>
        <label for="switch">RPi LED Control</label>
        <input type="checkbox" data-role="flipswitch" name="switch" id="ckLED">
    </form>
 </div>
</div>
</body>
</html>
'''


#Configure to input
GPIO.setup(pin_to_circuit, GPIO.IN)
run(host = '192.168.4.31', port = '8080')

while True:
    a = float(GPIO.input(pin_to_circuit))
    @route('/action', method='POST')
    #print(a)

GPIO.setwarnings(disable)

#UNFINISHED

def action():
    val = request.forms.get('strState')
    on = bool(int(val))
    GPIO.output(18, on) 


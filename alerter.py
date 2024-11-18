alert_failure_count = 0

def network_alert_stub(celcius):
 
    if celcius > 200:  
        return 500
    return 200


def alert_in_celcius(farenheit, network_alert):
   
    global alert_failure_count
    celcius = (farenheit - 32) * 5 / 9
    return_code = network_alert(celcius)
    if return_code != 200:
        alert_failure_count += 1


alert_in_celcius(400.5, network_alert_stub) 
alert_in_celcius(303.6, network_alert_stub)  


print(f"{alert_failure_count} alerts failed.")
print("All is well (maybe!)")

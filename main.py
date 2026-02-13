import random
import datetime
import os

def generate_app_logs(amount):
        
    apps = ['Frontend', 'Backend', 'Payment_Gateway', 'Database']
    levels = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
        
    generated_logs = []

    for i in range(amount):
        now = datetime.datetime.now()
        logs = {
            "time": now.strftime("%Y-%m-%d, %H:%M:%S"),
            "application": random.choice(apps),
            "level": random.choice(levels)
            }
        generated_logs.append(logs)

    return generated_logs

def get_critical_errors(log_list):
    critical_logs = []
    for log in log_list:
        status = log['level']
        if status == "CRITICAL" or status == "ERROR":
            critical_logs.append(log)
    return critical_logs
if __name__ == "__main__":

    log_list = generate_app_logs(10000)
    criticals = get_critical_errors(log_list)

    if not os.path.exists("logs"):
        os.makedirs('logs')

    file_date = datetime.date.today()
    file_name = f"logs/logs@[{file_date}].txt"
    with open(file_name, "w") as file:
        for log in criticals:
            file.write(f"ALERT@ [{log['time']}] {log['application']} is in {log['level']} status\n")
            #file.write(f"Total of {len(criticals)} servers are down\n")   

    with open(file_name, "r") as file:
        total = 0
        crit = 0
        err = 0
        for line in file:
            total += 1
            if "CRITICAL" in line: 
                crit += 1
            elif "ERROR" in line:
                err += 1
    
print('success')
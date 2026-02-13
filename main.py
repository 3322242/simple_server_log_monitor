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

def get_folder_size(folder_path):
    total = 0
    files = os.listdir(folder_path)
    for file in files:
        full_path = os.path.join(folder_path, file)
        size = os.path.getsize(full_path)
        total += size
    return total

if __name__ == "__main__":

    # 1. Створюємо дані
    log_list = generate_app_logs(10000)
    criticals = get_critical_errors(log_list)

    # 2. Перевіряємо папку
    if not os.path.exists("logs"):
        os.makedirs('logs')

    # 3. Записуємо файл
    file_date = datetime.date.today()
    file_name = f"logs/logs@[{file_date}].txt"
    with open(file_name, "w") as file:
        for log in criticals:
            file.write(f"ALERT@ [{log['time']}] {log['application']} is in {log['level']} status\n") 

    # 4. Читаємо файл і рахуємо помилки
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

    # 5. ФІНАЛ: Рахуємо розмір папки і виводимо на екран
    total_bytes = get_folder_size("logs")
    total_mb = total_bytes / (1024 * 1024)
    print(f"📊 Поточний розмір папки 'logs': {total_mb:.3f} MB")
    print('✅ Успішно завершено!')
import csv

def check_range(A):
    if int(A[0]) == 10 and int(A[1]) in range(0,256) and int(A[2]) in range(0,256) and int(A[3]) in range(0,256):
        return True
    elif int(A[0]) == 172 and int(A[1]) in range(16,32) and int(A[2]) in range(0,256) and int(A[3]) in range(0,256):
        return True
    elif int(A[0]) == 192 and int(A[1]) == 168 and int(A[2]) in range(0,256) and int(A[3]) in range(0,256):
        return True
    else:
        return False

with open("F:\\rough-Pie\\ip_split\\data.csv") as ips, open("F:\\rough-Pie\\ip_split\\ItoI.csv","w") as ips1, open("F:\\rough-Pie\\ip_split\\EtoI.csv","w") as ips2:
    i = 1 # flag for header
    
    reader = csv.DictReader(ips)
    for row in reader:
        if i == 1:
            keys = [ key for key in row.keys()]
            i = 0
            writer = csv.DictWriter(ips1,fieldnames=keys)
            writer.writeheader()
            writer2 = csv.DictWriter(ips2,fieldnames=keys)
            writer2.writeheader()
        
        if 'OutBound' in row["Rule Message"]:
            row["Source IP"],row["Destination IP"] = row["Destination IP"],row["Source IP"]
        src = row["Source IP"].split('.')
        dest = row["Destination IP"].split('.')


        if check_range(src):
            if check_range(dest):
                writer.writerow(row)
        else:
            if check_range(dest):
                writer2.writerow(row)
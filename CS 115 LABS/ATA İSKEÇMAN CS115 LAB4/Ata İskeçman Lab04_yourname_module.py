def findAuthor(fn1,fn2):
    input_file = open(fn1,"r")
    output_file = open(fn2,"w")
    for line in input_file:
        output_file.write(line[line.find("~")+1::])
    input_file.close()
    output_file.close()

def findAveragePrice(fn1, cityName, distances):
    input_file = open(fn1,"r")
    total = 0
    rest_num = 1
    average = 0
    for line in input_file:
        if cityName.lower() in line.lower():
            if  float(line[line.find(";",line.find(";") +1 ) + 1 :line.rfind(";"):]) <= distances:
                total += float(line[line.rfind(";")+1::]) 
                rest_num += 1
    average = total/(rest_num-1) if rest_num > 1 else 0
    if average > 0:
        return total/(rest_num-1)
    else:
        return average

            

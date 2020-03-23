def count_substring(string, sub_string):
    count=0  
    idx=None    
    for i in range(len(string)):
        if len(string)>len(sub_string):             
            idx=string.find(sub_string)            
            if (idx>=0):
                count += 1
            string=string[(idx+1):]
    return count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
// string = ABCDCDC
// sub_string = CDC
// OUTPUT = 2

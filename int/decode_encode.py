str = "geeksforgeeks"
    
# encoding string   
str_enc = str.encode('utf8')  
    
# printing the encoded string  
print ("The encoded string in base64 format is : ",)  
print (str_enc ) 
    
# printing the original decoded string   
print ("The decoded string is : ",)  
print (str_enc.decode('utf8', 'strict')) 
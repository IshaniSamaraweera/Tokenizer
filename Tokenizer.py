'''
Version : python3
S.A. Ishani
13000462
'''

#Assumption: Torkenizer tokenize the input file until it read a invalid charactor

import sys

#Initialization
line_number = 1 
num_array = []  #Stores integer and float values
text = "" #Store the currently reading string
file_name = "file.txt"  #Input file name
k=1   #Value to decide terminating
decimal_points = 0
start_of_line = 1 #Stores line number of the current reading token

#Open the input file and read it character by character
with open("file.txt") as input_file:
  while (k==1):
    charactor = input_file.read(1)
    
    #Terminate when it reach the end of the file
    if not charactor:
      print("End of the file reached")
      break
    
    #Genarate text token from a string within double quotations
    elif(charactor == "\"" and len(num_array) == 0):
      start_of_line = line_number
      charactor = input_file.read(1)
      if(charactor == "\n"):
        line_number += 1
        text = text + charactor
      
      while(charactor != "\""):
        if not charactor:
          print("Error occured..! Check the content of the input file in line number ",line_number) #Error of missing closing quote of a string
          k=0
          sys.exit() #Trminate the program
        text = text + charactor
        charactor = input_file.read(1)
        if(charactor == "\n"):
          line_number += 1
        
      if(k==1):  #check still the stored token is valid before print it
        #Print the text token and reset values
        print("Found a TEXT token :- ")
        print(text)
        print("Line number :- ",start_of_line,"\n")
        start_of_line = line_number
        text = ""
        
    #Genarate text token within single quatations
    elif(charactor == "\'" and len(num_array) == 0):
      charactor = input_file.read(1)
      if(charactor == "\n"):
        line_number += 1
        text = text + charactor
      
      while(not(charactor=="\'")):
        if not charactor:
          print("Error occured..! Check the content of the input file in line number ",line_number) #Error of missing closing quote of a string
          #break
          k=0
          sys.exit()
        text = text + charactor
        charactor = input_file.read(1)
        if(charactor == "\n"):
          line_number += 1

      if(k==1): #check still the stored token is valid before print it
        #Print the text token and reset values
        print("Found a TEXT token :- ")
        print(text)
        print("Line number :- ",start_of_line,"\n")
        start_of_line = line_number
        text = ""

    #When charactor is a digit input into a inum_array list
    elif (charactor.isdigit() == True or charactor == "."):
      start_of_line = line_number
      num_array.append(charactor)
      
    #Print the integer token after it read a space, a tab or a newline
    elif((charactor == " " or charactor == "\t") and len(num_array) > 0):
      for i in range(0,len(num_array)):
            if(num_array[i]=="."):
              decimal_points += 1

      if(decimal_points == 0 and len(num_array) > 0): #Check whether the token is an integer
        print("Found a INTEGER token :- ",end = "")
        for i in range(0,len(num_array)):
          print(num_array[i], end=" ")
        
        print("\nLine no = ",start_of_line, "\n") #Prints the line number
        start_of_line = line_number
        num_array = []
        continue
      
      elif(decimal_points == 1 and len(num_array) > 0 and num_array.index(".")>0): #Check whether the token is an float
            #print("ss",num_larray.index("."))
            print("Found a FLOAT token :- ",end = "")
            for i in range(0,len(num_array)):
              print(num_array[i], end=" ")
        
            print("\nLine number = ",start_of_line, "\n") #Prints the line number
            start_of_line = line_number
            num_array = []
            decimal_points = 0
            continue
          
      else: #Genarate an error when token has more than one decimal place
            print("Error occured..! Check the content of the input file in line number ",line_number)
            #k = 0
            break

    elif(charactor == " " or charactor == "\t"):
      continue

    #Torkanize when it read a newline charactor(only for integer and float values)  
    elif(charactor == '\n' ):
      if len(num_array) != 0:
          for i in range(0,len(num_array)):
            if(num_array[i]=="."):
              decimal_points += 1

          if(decimal_points == 0 and len(num_array) > 0): #Check whether the token is an integer
            print("Found a INTEGER token :- ",end = "")
            for i in range(0,len(num_array)):
              print(num_array[i], end=" ")
        
            print("\nLine number = ",start_of_line, "\n") #Prints the line number
            line_number += 1
            start_of_line = line_number
            num_array = []
            decimal_points = 0
            continue
          
          elif(decimal_points == 1 and len(num_array) > 0 and num_array.index(".")>0): #Check whether the token is an float
            print("Found a FLOAT token :- ",end = "")
            for i in range(0,len(num_array)):
              print(num_array[i], end=" ")
        
            print("\nLine number = ",start_of_line, "\n") #Prints the line number
            line_number += 1
            start_of_line = line_number
            num_array = []
            decimal_points = 0
            continue
          
          else: #Genarate an error when token has more than one decimal place
            print("Error occured..! Check the content of the input file in line number ",line_number)
            k = 0
            break
      else:
        line_number += 1
        start_of_line = line_number

    elif(len(num_array)>0 and text !=0):
      print("Error occured..! Check the content of the input file in line number ",line_number)
      #k = 0
      break
        
    else: #Genarate error when the file contains invalid charactors
      print("Error occured..! Check the content of the input file in line number ",line_number)
      #k = 0
      break

      
 

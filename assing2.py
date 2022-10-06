def accept_marks(A):
   n= int(input("Enter the total no. of student :"))
   for i in range(n) :
      while True :
         x = input("Enter the marks scored in FDS for student %d : "%(i+1))
         if(x == "AB"):
            x = -1 #indicates Absent Studnets
            break
         x = int(x)
         if(x >= 0 and x<= 30) :
            break
         else :
            print("Plz enter valid marks out of 30")
      A.append(x)
   print("Marks accepted and scored sucessfully");
   
def display_marks(A):
    print("\nMarks Scored in FDS")
    for i in range(len(A)) :
       if(A[i] == -1):
           print("\tStudent %d : AB"%(i+1))
       else :
           print("\tStudent %d : %d"%(i+1,A[i]))
            
def find_average_score_of_class(A) :
    sum = 0
    for i in range(len(A)) :
       if(A[i] != -1) :
          sum = sum + A[i]
    avg = sum/len(A)
    #display_marks(A)
    print("\nAverage score of class is %.2f\n\n"%avg)
    
def find_highest_and_lowest_score_of_class(A) :
    max =30
    min =-1
    for i in range(1,len(A)) :
       if(max > A[i]) :
         max = A[i]
         max_ind = i
       if(min < A[i] and A[i] != -1) :
         min = A[i]
         min_ind = i
    #display_marks(A)
    print("Highest Mark Score of class is %d "%(max))
    print("Lowest Mark Score of class is %d "%(min))
    
def find_count_of_absent_students(A) :
   count = 0
   for i in range(len(A)):
      if(A[i] == -1) :    
         count += 1
   #display_marks(A)
   print("\tAbsent Student Count = %d"%count)
         
def display_mark_with_highest_frequency(A) :
    freq = 0
    for i in range(len(A)) :
       count = 0
       if(A[i] != -1) :
          for j in range(len(A)):
             if(A[i] == A[j]) :
                count += 1
       if (freq < count) :
           Marks = A[i]
           freq = count 
    #display_marks(A)
    print("\nMarks with highest frequency is %d (%d)"%(Marks,freq))
    
def main():
   FDS_Marks = []
   
   print("\n")
   print("\t\t1 : Accept FDS Marks")
   print("\t\t2 : Average score of class")
   print("\t\t3 : Highest score and Lowest score of class")
   print("\t\t4 : Count of students who were absent for the test")
   print("\t\t5 : Display mark with highest frequency")
   print("\t\t6 : Exit\n")

   while True :
      ch = int(input("\nEnter your choice : "))
      print("\n")
      if (ch == 6):
                print("End if Program")
                quit()
      elif (ch == 1) :
         accept_marks(FDS_Marks)
         display_marks(FDS_Marks)
      elif (ch == 2):
         find_average_score_of_class(FDS_Marks)
      elif (ch == 3) :
         find_highest_and_lowest_score_of_class(FDS_Marks)
      elif (ch == 4) :
         find_count_of_absent_students(FDS_Marks)
      elif (ch == 5) :
         display_mark_with_highest_frequency(FDS_Marks)
      else :
         print("Wrong choice entered !! Try again")
         
main()

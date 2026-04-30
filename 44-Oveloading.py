#overloading - same class , same method but different parameters 

# public class Main {
#     public static void main(String[] args) {
#       System.out.println("Hello, World!");
#       addition(1,2);
#       addition(1,2,3);
#       addition(1,2,3,4);
#     }
#     // def addition(x,y):
#     public static void addition(int x, int y){
#       System.out.println(x+y);
#     }
    
#     public static void addition(int x, int y,int z){
#       System.out.println(x+y+z);
#     }
    
#     public static void addition(int x, int y,int z ,int a){
#       System.out.println(x+y+z+a);
#     }
    
# }

class Calculator : 
    def addition(self, a=None, b=None, c=None,d=None):
        if a != None and b != None and c != None and d != None:
            print(a+b+c+d)

        elif a !=None and b !=None and c!=None:
            print(a+b+c)
        
        elif a !=None and b !=None:
            print(a+b) 
        
        else :
            print("atlist 2 values are required")

cc=Calculator()
cc.addition(1,2)
cc.addition(1,2,3)
cc.addition(1,2,3,4)
cc.addition(1)
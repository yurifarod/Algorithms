

import java.util.*;

public class Main {
    public static void main(String[] args) {
      for(int i = 0; i < 5; i++){
        for(int j = 5; j > -5; j--){
          if(i+j > 5){
            break;
          }
          System.out.println(j);
        }
        System.out.println(i);
      }
  }
}



import java.util.Scanner;

//This code will show the predicted amount of e-waste after a certain number of years and will also show given a different rate of change how the total waste will be impacted over time. 
public class CodeComponent {

   public static void main(String []args) {
      System.out.println("Planned obsolescence produces tons of e-waste each year." + '\n' + "This program will give a explore the predition of how much e-waste is produced with a fixed rate of 6% per year as well as a comparison of of the e-waste amount with a given rate.");
      
      //ask the user for the rate of change for e-waste production
      System.out.println("Enter the number of years: ");
      Scanner input = new Scanner(System.in);
      int numYear = input.nextInt();
      input.nextLine();
     
      //ask the user for the rate of change for e-waste production
      System.out.println("Enter the rate of change for e-waste production: ");
      double userRate = input.nextDouble();
      double initial = calcTotaleWaste(numYear, 6);
      double newRate = calcTotaleWaste(numYear, userRate);
      displayYearlyeWaste(numYear);
      System.out.println();
      displayYearlyeWaste(numYear, userRate);
      System.out.println();
      amountSaved(initial, newRate);

    
    //each year, 40 million tons of e-waste is produced globally
    //we ask the user for how many years do you want to calculate how much of e-waste is produced
    //e-waste increases by 6% every year
   }
  
    // public static void calcTotalWaste(int years){
    //   double total;
    //   total = 40*Math.pow((1.06),(years-1));
    //   System.out.println("The predicted total amount of e-waste is: " + total + " tons.");
    // }

    //displays the e-Waste generated in each year
    public static void displayYearlyeWaste(int year){
      double yearTotal;
      double total = 0;
      for(int i = 0; i <= year; i++){
          yearTotal = calcYearlyeWaste(i);
          total += yearTotal; 
          System.out.println("In year " + (i + 2022) + ", the predcited amount of e-waste that year: " + yearTotal);
          System.out.println("The total e-waste in " + (i + 2022) + ": " + total);
      }
    }


    //displays the e-Waste generated in each year with user input rate
    public static void displayYearlyeWaste(int year, double rate){
      double yearTotal;
      double total = 0;
      for(int i = 0; i <= year; i++){
          yearTotal = calcYearlyeWaste(i, rate);
          total += yearTotal; 
          System.out.println("In year " + (i + 2022) + ", the predcited amount of e-waste that year: " + yearTotal);
          System.out.println("The total e-waste in " + (i + 2022) + ": " + total);
      }
    }

    //calculates the e-Waste generated each year
    public static double calcYearlyeWaste(int year){
      double yearTotal;
      yearTotal = 40*Math.pow((1.06),year);
      
      return yearTotal;
    }

    //calculates yearly e-Waste with user inputing the rate and the # of years
    public static double calcYearlyeWaste(int year, double rate){
      double yearTotal;
      yearTotal = 40*Math.pow((1 + (0.01 * rate)),year);
    
      return yearTotal;
    }

    //calculates the total number of waste with the given number of years and rate
    public static double calcTotaleWaste(int year, double rate){
      double yearTotal;
      double total = 0;
      for(int i = 0; i <= year; i++){
          yearTotal = calcYearlyeWaste(i, rate);
          total += yearTotal; 
      }
      return total;
    }

    //display the difference between the total amount of waste of two different models
    public static void amountSaved(double initialRate, double newRate){
      System.out.println("Total reduction of waste in million tons:" + (initialRate - newRate));
    }
}

package pe;

import java.util.ArrayList;

//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
//Find the sum of all the primes below two million.

public class SumOfPrimes {
	
	public long sumPrimesInRange(long start, long end)
	{
		long sum = 0;
		
		for(long i = start; i < end;i++)
		{
			if(checkIfPrime(i) == true)
			{
				sum += i;
			}
			else
			{
				sum += 0;
			}
		}
			
		return sum ;
		
	}
	
	
	public boolean checkIfPrime(long n) {
		
		if (n % 2 == 0 && n != 2|| n % 3 == 0 && n != 3|| n % 5 == 0 && n != 5|| n % 7 == 0 && n != 7) {
			return false;
		}
		for (long i = 7; i * i < n; i = i + 1) {
			if (n % i == 0 || n % (i + 2) == 0) {
				return false;
			}
		}

		return true;

	}
	
	public static void main(String[] args)
	{
		SumOfPrimes sumPrime = new SumOfPrimes();
		System.out.println(sumPrime.sumPrimesInRange(2, 2000000));
	}

}

#include <stdio.h>

int prime_c(int num)
{
	if (num <=1)
	{
		return 0;
	}
	
	if (num ==2)
	{
		return 1;
	}
	
	if (num%2 ==0)
	{
		return 0;
	}
	
	for (int i =3;i*i <=num;i +=2)
	{
		if(num%i ==0)
		{
			return 0;
		}
		return 1;
	}
}

int main()
{
	
	int n;
	printf("Enter a Positive interger n:");
	scanf("%d", &n);
	
	if (n<2)
	{
		printf("Unable to find prime in the specified range");
		return 0;
	}
	
	printf("Prime Numbers upto %d are:\n", n);
	for (int i =2;i <=n;i ++)
	{
		if (prime_c(i))
		{
			printf("%d ", i);
		}
	}
	printf("\n");
	return 0;
	
}


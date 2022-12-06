#include <iostream>  
using namespace std ;  
int sub(int A[] , int n , int sum )  
{  
    int initial_sum = A[0] , start = 0 , i ;    
    for ( i = 1 ; i <= n ; i++) 
    {  
        while ( initial_sum > sum && start < i - 1)
         {  
            initial_sum = initial_sum - A[ start ] ;  
            start++ ;  
        }  
        if ( initial_sum == sum && ((i-start)==5))
         {  
            cout<<"subarray is " ;
            for(int j=start;j<=i-1;j++)
            {
                cout<<A[j]<<" ";
            }
            return 1 ;  
        }  
        if (i < n)  
            initial_sum = initial_sum + A[ i ] ;  
    }   
    cout << " no subarray found\n" ;  
    return 0 ;  
}  
  
int main()  
{  
    int i,n , sum ;  
    cout <<"enter array size\n";  
    cin >> n ;  
    int A[n];
    cout <<"enter array\n" ;  
    for ( i = 0 ; i < n ; i++ )  
    {  
        cin >> A[i] ;  
    }  
    cout << "enter sum value\n";  
    cin >> sum ;  
    sub ( A , n , sum ) ;  
    return 0 ;  
}  
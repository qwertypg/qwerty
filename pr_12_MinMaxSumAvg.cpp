/*
 Implement Min, Max, Sum and Average operations using Parallel Reduction. 
Measure the performance of sequential and parallel algorithms. 
*/

#include<iostream>
#include<vector>
#include<omp.h>
using namespace std;

int main(){

    vector<int> a={1,2,3,4,5,6,7,8,9,10};

    int mn=a[0],mx=a[0],sum=0;
    double avg,s,e;

    // Sequential
    s=omp_get_wtime();

    for(int x:a){

        mn=min(mn,x);
        mx=max(mx,x);

        sum+=x;
    }

    avg=(double)sum/a.size();

    e=omp_get_wtime();

    cout<<"Sequential\n";
    cout<<"Min="<<mn<<"\nMax="<<mx;
    cout<<"\nSum="<<sum<<"\nAvg="<<avg;
    cout<<"\nTime="<<e-s<<"\n\n";

    // Reset
    mn=mx=a[0];
    sum=0;

    // Parallel
    s=omp_get_wtime();

#pragma omp parallel for reduction(min:mn) reduction(max:mx) reduction(+:sum)
    for(int i=0;i<a.size();i++){

        mn=min(mn,a[i]);
        mx=max(mx,a[i]);

        sum+=a[i];
    }

    avg=(double)sum/a.size();

    e=omp_get_wtime();

    cout<<"Parallel\n";
    cout<<"Min="<<mn<<"\nMax="<<mx;
    cout<<"\nSum="<<sum<<"\nAvg="<<avg;
    cout<<"\nTime="<<e-s;
}
#include<iostream>
#include<vector>
#include<algorithm>
#include<omp.h>
using namespace std;

void bubble(vector<int>& a){

    for(int i=0;i<a.size();i++){

#pragma omp parallel for
        for(int j=i%2;j<a.size()-1;j+=2)

            if(a[j]>a[j+1])
                swap(a[j],a[j+1]);
    }
}

void merge(vector<int>& a,int l,int m,int r){

    vector<int> t;
    int i=l,j=m+1;

    while(i<=m && j<=r)
        t.push_back(a[i]<a[j]?a[i++]:a[j++]);

    while(i<=m) t.push_back(a[i++]);
    while(j<=r) t.push_back(a[j++]);

    for(int k=l;k<=r;k++)
        a[k]=t[k-l];
}

void mergeSort(vector<int>& a,int l,int r){

    if(l>=r) return;

    int m=(l+r)/2;

#pragma omp parallel sections
    {
#pragma omp section
        mergeSort(a,l,m);

#pragma omp section
        mergeSort(a,m+1,r);
    }

    merge(a,l,m,r);
}

void print(vector<int> a){

    for(int x:a) cout<<x<<" ";
}

int main(){

    vector<int> a={9,5,1,4,3,8,2,7,6},
                b=a,c=a,d=a;

    double s,e;

#define RUN(x,msg) s=omp_get_wtime();\
x;\
e=omp_get_wtime();\
cout<<msg;\
print(x==bubble(a),a:x==mergeSort(d,0,d.size()-1),d:b);\
cout<<"\nTime: "<<e-s<<"\n\n";

    s=omp_get_wtime();
    sort(b.begin(),b.end());
    e=omp_get_wtime();
    cout<<"Seq Bubble: "; print(b);
    cout<<"\nTime: "<<e-s<<"\n\n";

    s=omp_get_wtime();
    bubble(a);
    e=omp_get_wtime();
    cout<<"Par Bubble: "; print(a);
    cout<<"\nTime: "<<e-s<<"\n\n";

    s=omp_get_wtime();
    sort(c.begin(),c.end());
    e=omp_get_wtime();
    cout<<"Seq Merge: "; print(c);
    cout<<"\nTime: "<<e-s<<"\n\n";

    s=omp_get_wtime();
    mergeSort(d,0,d.size()-1);
    e=omp_get_wtime();
    cout<<"Par Merge: "; print(d);
    cout<<"\nTime: "<<e-s;
}
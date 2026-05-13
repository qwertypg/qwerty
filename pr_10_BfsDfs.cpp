#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<omp.h>

using namespace std;

vector<int> g[10];
int vis[10];

// Sequential BFS
void seqBFS(int s){

    queue<int> q;

    q.push(s);
    vis[s]=1;

    while(!q.empty()){

        int n=q.front();
        q.pop();

        cout<<n<<" ";

        for(int x:g[n]){

            if(!vis[x]){

                vis[x]=1;
                q.push(x);
            }
        }
    }
}

// Parallel BFS
void parBFS(int s){

    queue<int> q;

    q.push(s);
    vis[s]=1;

    while(!q.empty()){

        int n=q.front();
        q.pop();

        cout<<n<<" ";

#pragma omp parallel for
        for(int i=0;i<g[n].size();i++){

            int x=g[n][i];

#pragma omp critical
            {
                if(!vis[x]){

                    vis[x]=1;
                    q.push(x);
                }
            }
        }
    }
}

// Sequential DFS
void seqDFS(int n){

    vis[n]=1;

    cout<<n<<" ";

    for(int x:g[n]){

        if(!vis[x])
            seqDFS(x);
    }
}

// Parallel DFS
void parDFS(int n){

    bool d=false;

#pragma omp critical
    {
        if(vis[n])
            d=true;

        else{

            vis[n]=1;
            cout<<n<<" ";
        }
    }

    if(d)
        return;

#pragma omp parallel for
    for(int i=0;i<g[n].size();i++){

        int x=g[n][i];

        if(!vis[x])
            parDFS(x);
    }
}

int main(){

    g[0]={1,2};
    g[1]={0,3,4};
    g[2]={0,5,6};
    g[3]={1};
    g[4]={1};
    g[5]={2};
    g[6]={2};

    double s,e;

#define RUN(x,msg) fill(vis,vis+10,0);\
s=omp_get_wtime();\
cout<<msg;\
x;\
e=omp_get_wtime();\
cout<<"\nTime: "<<e-s<<"\n\n";

    RUN(seqBFS(0),"Seq BFS: ")
    RUN(parBFS(0),"Par BFS: ")
    RUN(seqDFS(0),"Seq DFS: ")

    fill(vis,vis+10,0);

    s=omp_get_wtime();

    cout<<"Par DFS: ";

#pragma omp parallel
#pragma omp single
    parDFS(0);

    e=omp_get_wtime();

    cout<<"\nTime: "<<e-s;

    return 0;
}
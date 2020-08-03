#include <iostream>
using namespace std;

int main() {
int t,n1,m1,n2,m2;
int arr1[30][30];
int arr2[30][30];

cin>>t;
while(t--)
{
cin>>n1>>m1;
for(int i=0;i<n1;i++) { for(int j=0;j<m1;j++) 
cin>>arr1[i][j];

}
cin>>n2>>m2;
for(int i=0;i<n2;i++) {
    for(int j=0;j<m2;j++)
cin>>arr2[i][j];

}
int c[1000][1000];
for(int i=0;i<n2;i++) {
    for(int j=0;j<m2;j++) 
c[i][j]+=arr1[i][j]*arr2[i][j]; 
    cout<<c[i][j];
}
if(n2==m1) 
{for(int i=0;i<n2;i++) { for(int j=0;j<m2;j++)
cout<<c[i][j]<<" "; } cout<<endl; }
else {
    cout<<-1<<endl; } } return 0; }



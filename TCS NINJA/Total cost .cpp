#include<iostream>

using namespace std;
int main()
{
    
    int InteriorWall , ExteroirWall;
    cin>>InteriorWall>>ExteroirWall;
    float SurfaceInter[InteriorWall] , SurfaceExter[ExteroirWall];
    float SSurfaceIn=0,SSurfaceEx=0;
    for(int i=0;i<InteriorWall;++i)
    {
        cin>>SurfaceInter[i];
        SSurfaceIn+=SurfaceInter[i];
        
    }
    
    for(int i=0;i<ExteroirWall;++i)
    {
        cin>>SurfaceExter[i];
        SSurfaceEx+=SurfaceExter[i];
        
    }
    
    float Int , Ext;
    Int = 18*(SSurfaceIn);
    Ext = 12*(SSurfaceEx);
    cout<<(Int+Ext);
    
    
}
/*Question :- https://www.youtube.com/watch?v=DtUm_E-p0OU */
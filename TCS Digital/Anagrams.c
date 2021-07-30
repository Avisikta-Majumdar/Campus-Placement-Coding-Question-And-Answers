
#include <stdio.h>

int main()
{
    int i,j,array[128]={0};
    char s1[100],s2[100];
    scanf("%s %s",s1,s2);
    for(i=0;s1[i]!='\0';++i){
        array[s1[i]]++;
    }
    for(i=0;s2[i]!='\0';++i){
        array[s2[i]]--;
    }
    for(i=0;i<128;++i)
    {
        if(array[i]!=0)
        {
            printf("Not anagrams");
            return 0;
        }
    }
    printf("Anagrams");
    return 0;
}

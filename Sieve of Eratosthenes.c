#include <stdio.h>
#include <stdlib.h>

void create_array(int n, int *num_list);
void find_primes(int n, int *num_list);

int main(){
    int n, current=0;

    printf("Enter a number between 2-1000 to generate the list : ");
    scanf("%d", &n);
    if((n<2) || (n>1000)){
        printf("Wrong value, please try again\n");
        exit(1);
    }

    int *num_list = (int *)malloc(n*sizeof(int));

    printf("\n\n");
    create_array(n, num_list);
    find_primes(n, num_list);

    return 0;
}


void create_array(int n, int *num_list){
    if (num_list == NULL){
        printf("\nMemory is not available.\n");
        exit(1);
    }
    printf("Original list: ");
    for (int i=0; i<=n-2; i++){
        num_list[i] = i+2;                 //excluding 0 and 1
        printf("%d ", num_list[i]);
    }
    printf("\n\n\n");
}


void find_primes(int n, int *num_list){
    int current;
    for (int j=0; j<=n-2; j++){
        current = num_list[j];

        for (int i=j; (i<=n-2) && (current!=0); i+=current){
            if (num_list[i] != current){
                num_list[i] = 0;           //replacing the eliminated numbers with 0
            }
        }

        if (current !=0){
            printf(" multiples of '%d' are eliminated->\t", current);

            for (int x=0; x<=n-2; x++){
            if(num_list[x] != 0){          //replaced ones are omitted
                printf("%d ", num_list[x]);
            }
        }
        printf("\n");
        }
    }
}

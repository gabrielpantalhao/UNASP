#include <stdio.h>
#include <string.h>

int main() {
    
    int idade;

 printf("Digite a sua idade: ");
 scanf("%d", &idade);
 
  if(idade >= 18){
    printf("Você pode tirar a CNH. Você possui %d anos de idade.", idade);
  }else{
    printf("Você não pode tirar a CNH. Você possui %d anos de idade.", idade);
  }
 
    return 0;
}
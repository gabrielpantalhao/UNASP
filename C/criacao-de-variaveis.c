#include <stdio.h>
#include <string.h>

int main() {
    char nome[50];
    int idade;
    char endereco[150];
 
 printf("digite o seu nome completo: ");
 fgets(nome, sizeof(nome), stdin);
 nome[strcspn(nome, "\n")] = 0;
    
 printf("Digite a sua idade: ");
 scanf("%d", &idade);
 
 while(getchar() != '\n');
 
 printf("Digite o seu endereço: ");
 fgets(endereco, sizeof(endereco), stdin);
 endereco[strcspn(endereco, "\n")] = 0;
 
 printf("\nOlá, %s! Seja bem vindo!\n ", nome);
 printf("\nIdade: %d!\n", idade);
 printf("\nSeu endereço é %s\n ", endereco);
 
    return 0;
}
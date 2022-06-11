/**************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

***************************/

#include <stdio.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <time.h>

#define TAM_CATEGORIAS_SALARIO 100


void printSalario(std::string tipo_categoria, std::string nome_categoria, float valor_categoria) {
    std::cout << "Categoria - " << tipo_categoria << " - " << nome_categoria;
    printf(" ===> %.2f\n", valor_categoria);
}

float calculaEstatisticasSalario(int tamanho, float *valor_total_categoria) {
    float soma = 0;
    float maior = valor_total_categoria[0];
    float menor = valor_total_categoria[0];
    
    //somatória dos gastos
    for (int i = 0; i < tamanho; i++){
        soma = soma + valor_total_categoria[i];
        
        if (valor_total_categoria[i] > maior)
            maior = valor_total_categoria[i];

        if (valor_total_categoria[i] < menor)
            menor = valor_total_categoria[i];
    }
    
    printf("-----------------Gasto Total com Comida até o momento-----------------\n");
    printf("-=-=-=-=-=-=-=-=-= %.2f =-=-=-=-=-=-=-=-=-\n", soma);
    printf("-----------------Maior(es) Gasto(s) na Categoria Comida até o momento-----------------\n");
    printf("-=-=-=-=-=-=-=-=-= %.2f =-=-=-=-=-=-=-=-=-\n", maior);
    printf("-----------------Menor(es) Gasto(s) na Categoria Comida até o momento-----------------\n");
    printf("-=-=-=-=-=-=-=-=-= %.2f =-=-=-=-=-=-=-=-=-\n", menor);
    
    return soma;
}

int main()
{
    float total_salario_fixo_1 = 1000, total_salario_fixo_2 = 1142.80, total_vr_fixo = 700;
    float total_salario_inicio = 2385.54, total_vr_inicio;
    float total_salario_final = total_salario_inicio, total_vr_final = total_vr_inicio;
    float total_categoria_salario_sacolao, total_categoria_salario_marmitas, total_categoria_salario_bebida, total_categoria_salario_fastfood, total_categoria_salario_mercado, total_categoria_salario_uffbandejao;
    
    /*
    time_t mytime;
    mytime = time(NULL);
    struct tm tm = *localtime(&mytime);
    //printf("Data: %d/%d/%d/\n", tm.tm_mday, tm.tm_mon + 1, tm.tm_year + 1900);
    if(tm.tm_mday == 15) {
        if(tm.tm_wday == 0) {
            tm.tm_mday -= 2;
        }
        printf("\nDia da semana: %d\n\n", tm.tm_wday); //dia da semana de 0 (domingo) até 6 (sábado)
        total_salario_inicio += total_salario_fixo_1;
    }
    else if(tm.tm_mday == 31 || )
        total_salario_inicio += total_salario_fixo_2;
    */
    
    total_categoria_salario_sacolao = 25.58;
    total_categoria_salario_marmitas = 0;
    //total_categoria_salario_bebida = 17;
    total_categoria_salario_fastfood = 86.50;
    total_categoria_salario_mercado = 0;
    total_categoria_salario_uffbandejao = 5;
    
    // Inicializando String Array
    std::vector<std::string> categorias_salario = {"Comida", "Uber", "Bebida", "Passagem usando vale transporte", "Objetos para casa", "Objetos para PC", "Materiais escolares ou de desenho", "Roupas", "Aluguel", "Internet", "Dinheiro dado para amigos"};
    std::vector<std::string> tipo_salario_comida = {"Sacolão", "Marmitas", "Fast Food", "Mercado", "UFF | Bandejão"};
    float valor_salario_comida[tipo_salario_comida.size()] = {total_categoria_salario_sacolao, total_categoria_salario_marmitas, 
                                                total_categoria_salario_fastfood, 
                                                total_categoria_salario_mercado, total_categoria_salario_uffbandejao};
    

    
    
    
    printf("========================================================================\n");
    printf("SOFC - Sistema de Organização Financeira em Categorias\n");
    printf("Cálculos do período entre os dias 26/04/2022 - 28/05/2022\n");
    printf("Valor baseado nos gastos referentes ao Salário\n");
    printf("-----------------Salário ANTES do período-----------------\n");
    printf("-=-=-=-=-=-=-=-=-= %.2f =-=-=-=-=-=-=-=-=-\n", total_salario_inicio);
    printf("========================================================================\n\n\n");
    
    // Printar Strings
    //for (int i = 0; i < categorias_salario.size(); i++)
    //   std::cout << categorias_salario[i] << "\n";
        // Strings can be added at any time with push_back
    //categorias_salario.push_back("Yellow");
    
    for (int i = 0; i < tipo_salario_comida.size(); i++)
        printSalario(categorias_salario[0], tipo_salario_comida[i], valor_salario_comida[i]);
    
    total_salario_final -= calculaEstatisticasSalario(tipo_salario_comida.size(), valor_salario_comida);
    
    
    printf("Categoria - Dinheiro dado para amigos - 33.01\n");
    
    printf("\n\n\n========================================================================\n");
    printf("Cálculos do período entre os dias 26/04/2022 - 28/05/2022\n");
    printf("Valor baseado nos gastos referentes ao Salário\n");
    printf("-----------------Salário APÓS do período-----------------\n");
    printf("-=-=-=-=-=-=-=-=-= %.2f =-=-=-=-=-=-=-=-=-\n", total_salario_final);
    printf("========================================================================\n");
    
    
    printf("Valor baseado nos gastos referentes ao Vale Refeição\n");
    printf("Categoria - Comida - Sacolão\n");
    printf("Categoria - Comida - Marmitas\n");
    printf("Categoria - Comida - Fast food\n");
    printf("Categoria - Comida - Mercado\n");
    printf("Categoria - Comida - UFF\n");

    return 0;
}
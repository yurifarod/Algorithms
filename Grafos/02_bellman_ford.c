#include <stdio.h>
#include <limits.h>

#define MAX_VERTICES 100
#define INFINITO 99999

// Função para imprimir o array de distâncias construído
void printSolution(int dist[], int vertices) {
    printf("Vértice \tDistância da origem\n");

    for (int i = 0; i < vertices; i++) {
        if (dist[i] == INFINITO) {
            printf("%d \t\tInfinito\n", i);
        }
        else {
            printf("%d \t\t%d\n", i, dist[i]);
        }
    }
}

// Função que implementa o algoritmo de Bellman-Ford
void bellmanFord(int graph[MAX_VERTICES][MAX_VERTICES],
                 int src, int vertices) {

    int dist[MAX_VERTICES];

    // Inicializa todas as distâncias como infinito
    for (int i = 0; i < vertices; i++) {
        dist[i] = INFINITO;
    }

    // A distância da origem para ela mesma é zero
    dist[src] = 0;

    // Relaxa todas as arestas por vertices - 1 iterações
    for (int count = 0; count < vertices - 1; count++) {

        // Percorre todas as arestas do grafo
        for (int u = 0; u < vertices; u++) {
            for (int v = 0; v < vertices; v++) {

                // Verifica se existe uma aresta de u para v
                // e se u já possui uma distância conhecida
                if (graph[u][v] != INFINITO &&
                    u != v &&
                    dist[u] != INFINITO) {

                    // Verifica se o caminho passando por u
                    // é menor que a distância atual de v
                    if (dist[u] + graph[u][v] < dist[v]) {
                        dist[v] = dist[u] + graph[u][v];
                    }
                }
            }
        }
    }

    // Verifica a existência de ciclos de peso negativo
    for (int u = 0; u < vertices; u++) {
        for (int v = 0; v < vertices; v++) {

            if (graph[u][v] != INFINITO &&
                u != v &&
                dist[u] != INFINITO &&
                dist[u] + graph[u][v] < dist[v]) {

                printf("O grafo possui um ciclo de peso "
                       "negativo alcancavel a partir da origem.\n");
                return;
            }
        }
    }

    // Imprime o resultado final
    printSolution(dist, vertices);
}

int main() {
    int vertices;

    vertices = 5;

    int graph[MAX_VERTICES][MAX_VERTICES];

    // Criando a matriz de adjacência do grafo
    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {

            if (i == j) {
                graph[i][j] = 0;
            }
            else {
                graph[i][j] = INFINITO;
            }
        }
    }

    // Definindo as arestas e seus respectivos pesos
    graph[0][1] = 12;
    graph[0][3] = 87;
    graph[1][4] = 11;
    graph[2][0] = 19;
    graph[3][1] = 23;
    graph[4][2] = -2;
    graph[4][3] = 43;

    int source;

    printf("Entre com o vertice de origem da busca: ");
    scanf("%d", &source);

    // Validação do vértice de origem
    if (source < 0 || source >= vertices) {
        printf("Vertice de origem invalido!\n");
        return 1;
    }

    bellmanFord(graph, source, vertices);

    return 0;
}
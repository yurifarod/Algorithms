#include <stdio.h>
#include <limits.h>

#define MAX_VERTICES 100
#define INFINITO 99999

// Função para encontrar o vértice com a o valor mínimo de distância
int minDistance(int dist[], int sptSet[], int vertices) {
    int min = INFINITO, minIndex;

    for (int v = 0; v < vertices; v++) {
        if (!sptSet[v] && dist[v] < min) {
            min = dist[v];
            minIndex = v;
        }
    }

    return minIndex;
}

// Função para imprmir o array de distância construído
void printSolution(int dist[], int vertices) {
    printf("Vértice \tdistância da origem\n");
    for (int i = 0; i < vertices; i++) {
        printf("%d \t%d\n", i, dist[i]);
    }
}

// Função que implementa o algoritmo de Dijkstra para um Grafo (graph) e um vértice origem!
void dijkstra(int graph[MAX_VERTICES][MAX_VERTICES], int src, int vertices) {
    int dist[MAX_VERTICES]; // A saída deste array mantém a menor distância da origem para (src) para o vértice "i"
    int sptSet[MAX_VERTICES]; // sptSet[i] será verdadeiro se o vértice i estiver incluído na árvore do caminho mais curto ou se a distância mais curta de "src" para i for finalizada

    // Vamos inicializar as distancia como infinito e sptSet[i] como falsos!
    for (int i = 0; i < vertices; i++) {
        dist[i] = INFINITO;
        sptSet[i] = 0;
    }

    // A distancia da origem para ele mesmo é zero!
    dist[src] = 0;

    // Encontre o caminho mais curto para todos os vértices
    for (int count = 0; count < vertices - 1; count++) {
        // Selecione o vértice de distância mínima do conjunto de vértices ainda não processados.
        // u deverá ser sempre igual a src na primeira iteração.
        int u = minDistance(dist, sptSet, vertices);

        // Marque o vértice selecionado como processado
        sptSet[u] = 1;

        // Atualiza o valor dist dos vértices adjacentes do vértice escolhido.
        for (int v = 0; v < vertices; v++) {
        // Atualizar dist[v] somente se não estiver no sptSet, houver uma aresta de u para v,
		// e o peso total do caminho de src para v através de u for menor que o valor atual de dist[v]
            if (!sptSet[v] && graph[u][v] && dist[u] != INFINITO && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // Imprimindo o array de solução final
    printSolution(dist, vertices);
}

int main() {
    int vertices;

    vertices = 5;

    int graph[MAX_VERTICES][MAX_VERTICES];

    // Criando matriz de adjacência do grafo (graph)
    for(int i = 0; i < vertices; i++){
    	for(int j = 0; j < vertices; j++){
    		if(i == j){
    			graph[i][j] = 0;
    		}
    		else{
    			graph[i][j] = INFINITO;
    		}
    	}
    }
    graph[0][1] = 12;
    graph[0][3] = 87;
    graph[1][4] = 11;
    graph[2][0] = 19;
    graph[3][1] = 23;
    graph[4][2] = 10;
    graph[4][3] = 43;

    int source;
    printf("Entre com o vértice de origem da busca: ");
    scanf("%d", &source);

    dijkstra(graph, source, vertices);

    return 0;
}

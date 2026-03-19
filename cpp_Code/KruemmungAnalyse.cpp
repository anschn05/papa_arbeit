#include <iostream>
#include <vector>
#include <math.h>
# define M_PI           3.14159265358979323846 


// --- TODO ---

//Parameter
int l = 1100;
int b = 360;
double t = 3.6;
int step = 40;

double f(double x){
    return 2*x;
    //return 10*sin(2*M_PI*x/l);
};

void printVector(std::vector<double> PrintingVector){
    size_t n = PrintingVector.size();
    std::cout << "[";
    for(int i=0;i<n;i++){
        std::cout << PrintingVector[i] << ", ";
    }
    std::cout << "]\n";
};


template<typename T>
void printMatrix(const std::vector<std::vector<T>>& mat)
{
    for (const auto& row : mat)
    {
        for (const auto& val : row)
        {
            std::cout << val << "\t";
        }
        std::cout << "\n";
    }
}



int main(){

    // x-Werte generieren, mit aequidistanten Punkten, Anzahl: step
    std::vector<double> x_Werte(step);
    for(int i=0;i<step;i++){
        x_Werte[i] = i*l/(step-1);
    }
    //std::cout << x_Werte.size() << "\n";
    printVector(x_Werte);

    std::vector<double> z_Werte(step);
    for(int i=0;i<step;i++){
        z_Werte[i] = f(x_Werte[i]);
    }

    printVector(z_Werte);

    std::vector<std::vector<double>> xz_Array(step,std::vector<double> (2));
    
    //std::cout << x_Werte[3] << "\n";
    for(int i=0;i<step;i++){
        xz_Array[i][0] = x_Werte[i];
        xz_Array[i][1] = z_Werte[i];
    };

    printMatrix(xz_Array);

    """
    müssen noch:
    matrix  A = (x_i,y_i,1)_(i=1,...step) erstellen
    vector  b = -(x_i²+y_i²)_(i=1,...step) erstellen
    und LGS lösen für Radius und Kreismittelpunkt
    """

    return 0;
}

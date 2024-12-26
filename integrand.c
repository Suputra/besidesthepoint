#include <math.h>

double integrand1(int n, double *x) {
    return sqrt((x[0] * x[0]) + (x[1] * x[1]) - (x[2] * x[2]));
}

double integrand2(int n, double *x) {
    return sqrt(((1-x[0]) * (1-x[0])) + (x[1] * x[1]) - (x[2] * x[2]));
}

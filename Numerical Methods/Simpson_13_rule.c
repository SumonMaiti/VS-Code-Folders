#include <stdio.h>
#include <math.h>

// Define the function to be integrated
double f(double x) {
    return 1 / (1 + x*x);
}

// Implement Simpson's 1/3 rule
double simpson_13_rule(double lower_limit, double upper_limit, int num_intervals) {
    double h = (upper_limit - lower_limit) / num_intervals;
    double integral = f(lower_limit) + f(upper_limit);

    for (int i = 1; i < num_intervals; ++i) {
        if (i % 2 == 0) {
            integral += 2 * f(lower_limit + i * h);
        } else {
            integral += 4 * f(lower_limit + i * h);
        }
    }

    integral *= h / 3;
    return integral;
}

int main() {
    double lower_limit = 0;
    double upper_limit = 6;
    int num_intervals = 6;  // You can adjust the number of intervals for accuracy

    double result = simpson_13_rule(lower_limit, upper_limit, num_intervals);
    printf("The integral of 1/(1+x^2) from %.2f to %.2f using Simpson's 1/3 rule is approximately %.6f\n",
           lower_limit, upper_limit, result);

    return 0;
}

#include "model_arduino.h"
#include <string.h>

void score(double *input, double *output) {
    double var0[4];
    double arrStop[4] = {0.0, 1.0, 0.0, 0.0};
    double arrRight[4] = {0.0, 0.0, 1.0, 0.0};
    double arrLeft[4] = {0.0, 0.0, 0.0, 1.0};
    double arrForward[4] = {1.0, 0.0, 0.0, 0.0};
    
    if (input[0] <= 0.5) {
        if (input[1] <= 0.5) {
            memcpy(var0, arrStop, 4 * sizeof(double));
        } else {
            memcpy(var0, arrRight, 4 * sizeof(double));
        }
    } else {
        if (input[1] <= 0.5) {
            memcpy(var0, arrLeft, 4 * sizeof(double));
        } else {
            memcpy(var0, arrForward, 4 * sizeof(double));
        }
    }
    memcpy(output, var0, 4 * sizeof(double));
}



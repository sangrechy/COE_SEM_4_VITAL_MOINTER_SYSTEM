#include <stdio.h>
#include "fusion_predict.h"

int main()
{
    int ecg_class = 0;
    int stress_class = 1;

    int final_status =
        fusion_predict(
            ecg_class,
            stress_class
        );

    printf("ECG Class     = %d\n", ecg_class);
    printf("Stress Class  = %d\n", stress_class);
    printf("Final Status  = %d\n", final_status);

    return 0;
}

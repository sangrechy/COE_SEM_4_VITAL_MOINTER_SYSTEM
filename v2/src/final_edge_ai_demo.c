#include <stdio.h>

#include "ecg_predict.h"
#include "stress_predict.h"
#include "fusion_predict.h"

int main()
{
    int ecg_class =
        ecg_predict(
            40.0,
            0.10,
            0.05,
            0.10
        );

    int stress_class =
        stress_predict(
            70.0,
            5.0,
            36.8,
            0.3
        );

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

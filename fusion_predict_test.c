#include <stdio.h>

int fusion_predict(
    int ecg_class,
    int stress_class
)
{
    if(ecg_class == 0 && stress_class == 0)
        return 0;   // HEALTHY

    if(ecg_class == 0 && stress_class == 1)
        return 1;   // STRESSED

    if(ecg_class != 0 && stress_class == 0)
        return 2;   // CARDIAC ALERT

    return 3;       // HIGH RISK
}

int main()
{
    int ecg_class = 5;
    int stress_class = 1;

    int result =
        fusion_predict(
            ecg_class,
            stress_class
        );

    printf("Fusion Result = %d\n", result);

    return 0;
}

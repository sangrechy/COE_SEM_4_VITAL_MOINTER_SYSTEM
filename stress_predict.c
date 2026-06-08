#include "stress_predict.h"

int stress_predict(
    float heart_rate,
    float hrv,
    float body_temperature,
    float motion_level
)
{
    float features[4];

    features[0] = heart_rate;
    features[1] = hrv;
    features[2] = body_temperature;
    features[3] = motion_level;

    /*
        Forest inference will be connected here
        using stress_forest_export.c
    */

    return STRESS_BASELINE;
}

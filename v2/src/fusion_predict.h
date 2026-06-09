#ifndef FUSION_PREDICT_H
#define FUSION_PREDICT_H

#define HEALTHY 0
#define STRESSED 1
#define CARDIAC_ALERT 2
#define HIGH_RISK 3

int fusion_predict(
    int ecg_class,
    int stress_class
);

#endif

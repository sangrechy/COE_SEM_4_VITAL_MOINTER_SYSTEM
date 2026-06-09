#include <stdio.h>

#include "ecg_predict.h"
#include "stress_predict.h"
#include "fusion_predict.h"

int main()
{
    printf("%d\n",
        fusion_predict(
            ecg_predict(60.0,0.2,0.1,0.3),
            stress_predict(75.0,0.25,36.8,1200.0)
        )
    );

    return 0;
}

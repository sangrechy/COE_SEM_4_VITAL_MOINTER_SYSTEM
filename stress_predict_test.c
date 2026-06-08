#include <stdio.h>

#include "v2/ml/v1/stress/results/stress_forest_export.c"

int predict_tree(
    const int *feature,
    const float *threshold,
    const int *left,
    const int *right,
    const int *value,
    float x[])
{
    int node = 0;

    while(feature[node] != -2)
    {
        if(x[feature[node]] <= threshold[node])
            node = left[node];
        else
            node = right[node];
    }

    return value[node];
}

int main()
{
    float sample[4] =
    {
        120.0,
        25.0,
        38.5,
        3.0
    };

    int votes[4] = {0};

    votes[predict_tree(feature_0,threshold_0,left_0,right_0,value_0,sample)]++;
    votes[predict_tree(feature_1,threshold_1,left_1,right_1,value_1,sample)]++;
    votes[predict_tree(feature_2,threshold_2,left_2,right_2,value_2,sample)]++;
    votes[predict_tree(feature_3,threshold_3,left_3,right_3,value_3,sample)]++;
    votes[predict_tree(feature_4,threshold_4,left_4,right_4,value_4,sample)]++;
    votes[predict_tree(feature_5,threshold_5,left_5,right_5,value_5,sample)]++;
    votes[predict_tree(feature_6,threshold_6,left_6,right_6,value_6,sample)]++;
    votes[predict_tree(feature_7,threshold_7,left_7,right_7,value_7,sample)]++;
    votes[predict_tree(feature_8,threshold_8,left_8,right_8,value_8,sample)]++;
    votes[predict_tree(feature_9,threshold_9,left_9,right_9,value_9,sample)]++;
    votes[predict_tree(feature_10,threshold_10,left_10,right_10,value_10,sample)]++;
    votes[predict_tree(feature_11,threshold_11,left_11,right_11,value_11,sample)]++;
    votes[predict_tree(feature_12,threshold_12,left_12,right_12,value_12,sample)]++;
    votes[predict_tree(feature_13,threshold_13,left_13,right_13,value_13,sample)]++;
    votes[predict_tree(feature_14,threshold_14,left_14,right_14,value_14,sample)]++;
    votes[predict_tree(feature_15,threshold_15,left_15,right_15,value_15,sample)]++;
    votes[predict_tree(feature_16,threshold_16,left_16,right_16,value_16,sample)]++;
    votes[predict_tree(feature_17,threshold_17,left_17,right_17,value_17,sample)]++;
    votes[predict_tree(feature_18,threshold_18,left_18,right_18,value_18,sample)]++;
    votes[predict_tree(feature_19,threshold_19,left_19,right_19,value_19,sample)]++;

    int best = 0;

    for(int i=1;i<4;i++)
    {
        if(votes[i] > votes[best])
            best = i;
    }

    printf("Predicted Stress Class = %d\n", best);

    return 0;
}

def SAVE_RESULT(best_trial, INPUT_PATH, OUTPUT_DIR) :

    mixture = best_trial.get_mixture()
    num_of_clusters = best_trial.get_num_of_clusters()

    report = "num of clone\tMean VAF of each clone\n"
    report += f"{num_of_clusters}\t"
    
    for j in range(num_of_clusters) :
        report += f"clone {j}:"
        for i in range(len(mixture)):
            report += str(mixture[i, j]) +","

        report += "|"

    print("************** RESULT REPORT ***************")
    print(f"There are {num_of_clusters} clones in this sample")
    print(report)

    with open(OUTPUT_DIR + "/report.txt", 'w') as outfile :
        outfile.write(report)

        

import pandas as pd
import matplotlib.pyplot as plt


def print_answers_for_fourth_stage(first, second, third, fourth, fifth):
    print("The answer to the 1st question is", first)
    print("The answer to the 2nd question is", second)
    print("The answer to the 3rd question is", third)
    print("The answer to the 4th question is", fourth)
    print("The answer to the 5th question is", fifth[1] + ",", fifth[0], "blood tests")


if __name__ == "__main__":
    # pd.set_option('display.max_columns', 8)
    pd.set_option('display.max_columns', 14)
    general_df = pd.read_csv(
        "/Users/aragonerua/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/general.csv")
    prenatal_df = pd.read_csv(
        "/Users/aragonerua/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/prenatal.csv")
    sports_df = pd.read_csv(
        "/Users/aragonerua/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/sports.csv")

    # First Stage
    '''
    print(general_df.head(20), prenatal_df.head(20), sports_df.head(20), sep="\n")
    '''

    prenatal_df.rename(columns={"HOSPITAL": "hospital", "Sex": "gender"}, inplace=True)
    sports_df.rename(columns={"Hospital": "hospital", "Male/female": "gender"}, inplace=True)
    general_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
    general_df.drop(columns="Unnamed: 0", inplace=True)

    # Second Stage
    '''
    print(pd.DataFrame.sample(general_df, n=20, random_state=30))
    '''
    general_df.dropna(axis=0, thresh=1, inplace=True)
    general_df["gender"].replace(["man", "male", "woman", "female"], ["m", "m", "f", "f"], inplace=True)
    general_df.fillna(
        {"gender": "f", "bmi": 0, "diagnosis": 0, "blood_test": 0, "ecg": 0, "ultrasound": 0, "mri": 0, "xray": 0,
         "children": 0, "months": 0}, inplace=True)

    # Third Stage
    '''
    print(general_df.shape)
    print(general_df.sample(n=20, random_state=30))
    '''

    first_answer = general_df["hospital"].value_counts().idxmax()  # first answer
    second_answer = round(general_df.query("hospital == 'general' & diagnosis == 'stomach'").shape[0] /
                          general_df.query("hospital == 'general'").shape[0], 3)  # second answer
    third_answer = round(general_df.query("hospital == 'sports' & diagnosis == 'dislocation'").shape[0] /
                         general_df.query("hospital == 'sports'").shape[0], 3)  # third answer
    fourth_answer = general_df[general_df.hospital == "general"].age.median() - \
                    general_df[general_df.hospital == "sports"].age.median()  # fourth answer

    blood_test_number_taken = dict()
    hospitals = ['general', 'prenatal', 'sports']
    for hosp_name in hospitals:
        blood_test_number_taken.update({general_df.loc[:, ["hospital", "blood_test"]].query(
            "hospital == @hosp_name").replace(["t", "f"], [1, -1]).query("blood_test == 1").shape[0]: hosp_name})
    fifth_answer = list()  # fifth answer
    fifth_answer.append(max(blood_test_number_taken.keys()))
    fifth_answer.append(blood_test_number_taken.get(max(blood_test_number_taken.keys())))

    # Fourth Stage
    '''
    print_answers_for_fourth_stage(first_answer, second_answer, third_answer, fourth_answer, fifth_answer)
    '''

    # Fifth Stage

    patient_ages = list(int(patient_age) for patient_age in general_df.age)
    bins = [0, 15, 35, 55, 70, 80]
    plt.hist(patient_ages, color="orange", edgecolor="white", bins=bins)
    plt.show()

    dict_of_diagnosis = dict(general_df.diagnosis.value_counts())
    # print(dict_of_diagnosis.values())
    # print(dict_of_diagnosis.keys())
    plt.pie(dict_of_diagnosis.values(), labels=dict_of_diagnosis.keys())
    plt.show()

    general_heights = list(general_df.query("hospital == 'general'").height)
    prenatal_heights = list(general_df.query("hospital == 'prenatal'").height)
    sports_heights = list(general_df.query("hospital == 'sports'").height)
    data_list = [general_heights, prenatal_heights, sports_heights]
    fig, axes = plt.subplots()
    axes.set_xticks((1, 2, 3))
    axes.set_xticklabels(("General", "Prenatal", "Sports"))
    plt.violinplot(data_list)
    plt.show()

    print("The answer to the 1st question: 15-35")
    print("The answer to the 2nd question: pregnancy")
    print("The answer to the 3rd question: It's because most of sports' hospital patients are youth and they do a lot of sports, so they eat more than other groups of people and eventually they are bigger")

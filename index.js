function check_remaining_credits (classes, curriculum) {
    let length = curriculum.length
    let lectures_credits_taken = new Array(length)

    for (let i=0; i<classes.length; i++) {
        for (let j=0; j<length; j++) {
            if ( Object.values(curriculum[i]).includes(classes[i]['name']) ) {
                lectures_credits_taken[i] += classes[i]['credit']
                break;
            }
        }
    }
    return lectures_credits_taken;
}

function which_division_remains (student_ID_list, GE_list) {
    for (let i=0; i<GE_list.length; i++) {
        student_ID_list[i] -= GE_list[i];
    }
}

console.log(window.localStorage.getItem('subject_list'))


// data = "csv"
let data = []

let major_classes = []
let GE_classes = []

let total_classes_names = []

// let temp = [1,2,3]
// for (vari of temp) {
//     console.log(vari)
// }

for (row of odd_rows) {
    let lecture = {'name':row[4],'classification':row[5], 'credit':int(row[6]), 'grade':row[8]};
    total_classes_names.push(row[4])

    if (row[6] === 'P') {
        lecture['grade'] = 4.5; // needs to be fixed, don't count this into GPA
    }
    if (row[6] === 'F') {
        lecture['grade'] = 0.0;
    }
    if (lecture['classification'] === '전공') {
        major_classes.push(lecture);
    }
    if (lecture['classification'] === '교양') {
        GE_classes.push(lecture);
    }
}

let total_credits_major = 0;
let total_credits_GE = 0;

let GPA_major = 0.0;
let GPA_GE = 0.0;
let GPA_total = 0.0;

for (course of major_classes) {
    total_credits_major += course['credit'];
    GPA_major += course['credit'] * course['grade'];
}

for (course of GE_classes) {
    total_credits_GE += course['credit'];
    GPA_GE += course['credit'] * course['grade'];
}

GPA_total = (GPA_major + GPA_GE) / (total_credits_major + total_credits_GE);
GPA_major /= total_credits_major;
GPA_GE /= total_credits_GE

let experiment_credit = 0.0 // 실험실습.
let major_core_credit = 0.0 // 전공코어 (or 전공핵심).
let major_credit = 0.0 // 전공일반 (or 전공심화).

if (admission_year >= 2021) {
    experiment_credit = 6
    major_core_credit = 36
    major_credit = 21
    for (lecture of major_classes) {
        if (newSoft[0].includes(lecture['name'])) {
            major_core_credit -= lecture['credit']
        }
        if (newSoft[1].includes(lecture['name'])) {
            major_credit -= lecture['credit']
        }
        if (newSoft[2].includes(lecture['name'])) {
            experiment_credit -= lecture['credit']
        }
    }
}

if (admission_year < 2021) {
    experiment_credit = 14
    major_core_credit = 27
    major_credit = 24
    for (lecture of major_classes) {
        if (oldSoft[0].includes(lecture['name'])) {
            major_core_credit -= lecture['credit']
        }
        if (oldSoft[1].includes(lecture['name'])) {
            major_credit -= lecture['credit']
        }
        if (oldSoft[2].includes(lecture['name'])) {
            experiment_credit -= lecture['credit']
        }
    }
}

let curriculum = null;
let student_ID_list = [];
let GE_16_list = [2,2,4,2,4,4,2,3,3,3,21]
let GE_17_19_list = [2,2,4,2,4,2,3,3,3,24]
let GE_20_list = [2,3,4,3,8,6,3,3,3,18]
let GE_21_22_list = [22,3,4,3,11,6,6,18]
let GE_list;

if (admission_year <= 2016) {
    curriculum = sixteenVersion;
    GE_list = GE_16_list;

}
if (admission_year > 2016 && admission_year <= 2019) {
    curriculum = seventeenVersion;
    GE_list = GE_17_19_list;
}
if (admission_year === 2020) {
    curriculum = sixteenVersion;
    GE_list = GE_20_list;
}
if (admission_year > 2020) {
    curriculum = sixteenVersion;
    GE_list = GE_20_21_list;
}

student_ID_list = check_remaining_credits(GE_classes, curriculum);
which_division_remains(student_ID_list, GE_list);

// 여기는 파이썬으로 file에 write하는 방식.

// result_path = "./sample_data/" +  student_ID + "_result.txt"
// f = open(result_path, "w")
// f.write("student ID: %d\n\n" % int(student_ID))
// f.write("GPA_total: %f\n" % GPA_total)
// f.write("GPA_major: %f\n" % GPA_major)
// f.write("GPA_GE: %f\n" % GPA_GE)
// f.write("\n")
// f.write("credits_total: %d\n" % (total_credits_major + total_credits_GE))
// f.write("credits_major: %d\n" % total_credits_major)
// f.write("credits_GE: %d\n" % total_credits_GE)
// f.write("\n")
// f.write("remaining_major_core_credit: %d\n" % major_core_credit)
// f.write("remaining_major_credit: %d\n" % major_credit)
// f.write("remaining_experiment_credit: %d\n" % experiment_credit)
// f.write("\nGE left:\n")
// for i in range(len(student_ID_list)):
//     # f.write("%d " % student_ID_list[i])
//     if student_ID_list[i] < 0:
//         curriculum_name = list(curriculum[i].keys())[0]
//         f.write("%s: " %  curriculum_name)
//         curriculum_courses = curriculum[i][curriculum_name]
//         for item in curriculum_courses:
//             if item not in total_classes_names:
//                 f.write("%s " % item)
//         f.write("\n")

// f.close()
